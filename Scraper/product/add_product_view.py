from django.shortcuts import render
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Categorie
from logs.models import Log
from .serializers import AddProductSerializer
import requests
import json
from io import BytesIO
from django.core.files import File
from urllib.parse import urlparse


class FileUploadForm(forms.Form):
    file = forms.FileField()
    category = forms.CharField(max_length=100)
    original_store = forms.CharField(max_length=100)
    
@user_passes_test(lambda u: u.is_staff)
def upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            category = form.cleaned_data['category']
            original_store = form.cleaned_data['original_store']
            output = process_data(file, category, original_store, request.user)
            return render(request, 'product/add_product.html', {'form': form, 'output': output})
    else:
        form = FileUploadForm()
    return render(request, 'product/add_product.html', {'form': form})


def process_data(file, categorie, store, user ):
    try:
        cate = []
        ret = {"details": "Succefully uploaded all products"}
        #check if categorie exist, if not create one
        for i in [j.strip().lower() for j in categorie.split(',')]:
            c = Categorie.objects.filter(categorie_name=i).first()
            if not c:
                new_categorie = Categorie(categorie_name=i)
                new_categorie.save()
                cate.append(new_categorie.id)
            else:
                cate.append(c.id)
        for prod in json.loads(s=file.read().decode('ascii')):
            resp = requests.get(prod['photo'])
            #if image found download it, else insert image not found in ret
            if resp.status_code == 200:
                #download image
                parsed_url = urlparse(prod['photo'])
                filename = parsed_url.path.split('/')[-1]
                img = File(BytesIO(resp.content),name=filename)
                #insert image in the object
                prod['photo'] = img
                prod['original_store'] = store.lower()
                prod['brand'] = prod['brand'].lower()
                prod['categorie'] =  cate
                #check if the data is correct, if so inset it in database
                prod_serilizer = AddProductSerializer(data=prod)
                if prod_serilizer.is_valid():
                    prod_serilizer.save()
            else:
                #if photo nout found
                ret[prod['full_name']] = "picture not found"
        log = Log(user=user, action="Added new products succefully")
        log.save()
        return ret
    except:
        #if there was an issue
        log = Log(user=user, action="Failed to add new products")
        log.save()
        return {"details": "json file contains issues"}
