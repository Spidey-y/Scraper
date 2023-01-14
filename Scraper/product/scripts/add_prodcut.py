from ..models import Product, Categorie
from logs.models import Log
from ..serializers import AddProductSerializer
import requests
import json
from io import BytesIO
from django.core.files import File
from urllib.parse import urlparse
import requests


def AddProduct(prod, store, cate, maxVal, more, less):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    try:
        resp = requests.get(prod['photo'], headers=headers)
    except:
        pass
    # if image found download it, else insert image not found in ret
    if resp.status_code == 200:
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
        prod['categorie'] = cate
        # check if the data is correct, if so inset it in database
        instc = Product.objects.filter(full_name=prod).first()
        if instc:
            update = AddProductSerializer(instc, data=prod)
            if update.is_valid():
                update.save()
        else:
            prod_serilizer = AddProductSerializer(data=prod)
            if prod_serilizer.is_valid():
                    prod_serilizer.save()