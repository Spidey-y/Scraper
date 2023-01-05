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
from product.scripts.sephora import scrap_sephora
from product.scripts.shein import scrap_shein
from product.scripts.aliexpress import scrap_aliexpress


class FileUploadForm(forms.Form):
    categories = forms.CharField(label='Categories (separated by , )', max_length=100)
    original_store = forms.ChoiceField(label='Original store',
                                       choices=[('amazon', 'Amazon'), ('aliexpress', 'AliExpress (USD)'),
                                                ('sephora', 'Sephora (USD)'),
                                                ('shein', 'Shein')])
    urls = forms.CharField(label='URLs (seperated by newline)', widget=forms.Textarea)
    percentage = forms.FloatField()
    max_value = forms.FloatField(label="Max price value (DZD)")
    more = forms.FloatField(label="Extra cost if more (DZD)")
    less = forms.FloatField(label="Extra cost if less (DZD)")


@login_required(login_url='/admin/login')
@user_passes_test(lambda u: u.is_staff)
def upload_view(request):
    """
    Add products, only for admin, retrieve the form, the scrap the urls
    """
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            urls = form.cleaned_data['urls']
            category = form.cleaned_data['categories']
            original_store = form.cleaned_data['original_store']
            percentage = form.cleaned_data['percentage']
            maxVal = form.cleaned_data['max_value']
            more = form.cleaned_data['more']
            less = form.cleaned_data['less']
            output = process_data(urls, category, original_store, request.user, percentage, maxVal, more, less)
            return render(request, 'product/add_product.html', {'form': form, 'output': output})
    else:
        form = FileUploadForm()
    return render(request, 'product/add_product.html', {'form': form})


def process_data(urls, categorie, store, user, perc, maxVal ,more, less):
    """
    We scape entire page, then send data to serializer, if everything is ok, add it to db
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
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
            #pick the store (scraping function)
            for url in urls.split("\r\n"):
                if store=="amazon":
                    products = scrape_amazon(url, perc)
                elif store == "shein":
                    products = scrap_shein(url, perc)
                elif store == "sephora":
                    products = scrap_sephora(url, perc)
                elif store == "aliexpress":
                    products = scrap_aliexpress(url, perc)
                else:
                    break

                for prod in products:
                        resp = requests.get(prod['photo'], headers=headers)
                        # if image found download it, else insert image not found in ret
                        if resp.status_code == 200:
                            try:
                                # download image
                                parsed_url = urlparse(prod['photo'])
                                filename = parsed_url.path.split('/')[-1]
                                img = File(BytesIO(resp.content), name=filename)
                                # insert image in the object
                                prod['photo'] = img
                                if prod['price'] > maxVal:
                                    prod['price'] += more
                                else:
                                    prod['price'] += less
                                prod['original_store'] = store.lower()
                                prod['brand'] = prod['brand'].lower()
                                prod['categorie'] = cates
                                # check if the data is correct, if so inset it in database
                                instc = Product.objects.filter(full_name=prod).first()
                                if instc:
                                    update = AddProductSerializer(instc, data=prod)
                                    if update.is_valid():
                                        update.save()
                                        continue
                                else:
                                    prod_serilizer = AddProductSerializer(data=prod)
                                    if prod_serilizer.is_valid():
                                            prod_serilizer.save()
                                    else:
                                        ret[prod['full_name']] = prod_serilizer.errors
                            except:
                                ret[prod['full_name']] = 'product wasn\'t added'
                        else:
                            # if photo nout found
                            ret[prod['full_name']] = "picture not found"
        #log the action
        log = Log(user=user, action="Added new products succefully")
        log.save()
        ret["details"] = "Upload is over"
        return ret
    except:
        # if there was an issue
        log = Log(user=user, action="Failed to add new products")
        log.save()
        return {"details": "either url is incorrect or url blocked by host"}
