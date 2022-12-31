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
from product.scripts.amazon import scrape_amazon


class FileUploadForm(forms.Form):
    categories = forms.CharField(label='Categories (separated by , )', max_length=100)
    original_store = forms.ChoiceField(label='Original store',
                                       choices=[('amazon', 'Amazon'), ('aliexpress', 'AliExpress'),
                                                ('sephora', 'Sephora'),
                                                ('shein', 'Shein')])
    urls = forms.CharField(label='URLs (seperated by newline)', widget=forms.Textarea)
    percentage = forms.FloatField()


@login_required(login_url='/admin/login')
@user_passes_test(lambda u: u.is_staff)
def upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            urls = form.cleaned_data['urls']
            category = form.cleaned_data['categories']
            original_store = form.cleaned_data['original_store']
            percentage = form.cleaned_data['percentage']
            output = process_data(urls, category, original_store, request.user, percentage)
            return render(request, 'product/add_product.html', {'form': form, 'output': output})
    else:
        form = FileUploadForm()
    return render(request, 'product/add_product.html', {'form': form})


def process_data(urls, categorie, store, user, perc):
    try:
        cates = []
        ret = {}
        # check if categorie exist, if not create one
        for i in [j.strip().lower() for j in categorie.split(',')]:
            c = Categorie.objects.filter(categorie_name=i).first()
            if not c:
                new_categorie = Categorie(categorie_name=i)
                new_categorie.save()
                cates.append(new_categorie.id)
            else:
                cates.append(c.id)
        try:
            for url in urls.split("\r\n"):
                if store=="amazon":
                    products = scrape_amazon(url, perc)
                for prod in products:
                    resp = requests.get(prod['photo'])
                    # if image found download it, else insert image not found in ret
                    if resp.status_code == 200:
                        # download image
                        parsed_url = urlparse(prod['photo'])
                        filename = parsed_url.path.split('/')[-1]
                        img = File(BytesIO(resp.content), name=filename)
                        # insert image in the object
                        prod['photo'] = img
                        prod['original_store'] = store.lower()
                        prod['brand'] = prod['brand'].lower()
                        prod['categorie'] = cates
                        # check if the data is correct, if so inset it in database
                        prod_serilizer = AddProductSerializer(data=prod)
                        if prod_serilizer.is_valid():
                            instc = Product.objects.filter(full_name=prod_serilizer.data['full_name']).first()
                            if instc:
                                update = AddProductSerializer(instc, data=prod)
                                if update.is_valid():
                                    update.save()
                            else:
                                prod_serilizer.save()
                        else:
                            ret[prod['full_name']] = prod_serilizer.errors
                    else:
                        # if photo nout found
                        ret[prod['full_name']] = "picture not found"
        except:
            ret[url] = 'invalid url'

        log = Log(user=user, action="Added new products succefully")
        log.save()
        ret["details"] = "Upload is over"
        return ret
    except:
        # if there was an issue
        log = Log(user=user, action="Failed to add new products")
        log.save()
        return {"details": "either url is incorrect or url blocked by host"}
