from rest_framework.response import Response
from rest_framework import status, viewsets, generics, permissions, parsers, filters, pagination
from .serializers import ProductSeedingSerializer, ProductSerializer, CategorieSerializer, BrandSerializer, StoreSerializer, OrderSerializer, GetOrderSerializer, AddProductSerializer
import json
import requests
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .models import Categorie, Product, Order
from logs.models import Log
from io import BytesIO
from django.core.files import File
from urllib.parse import urlparse
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class AddProductView(generics.GenericAPIView):
    """
    Add produts from json file
    If categorie not found in databse, it will be created
    status 201 if file correct and uploaded to db
    400 if no file provided, wrong file format
    """
    #define permission and parsers
    parser_classes = (parsers.MultiPartParser,parsers.FormParser)
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ProductSeedingSerializer
    def post(self, request):
        #If a file not provided return 400
        if not request.FILES.get("file"):
            return Response({"details": "Provide a json file"}, status=status.HTTP_400_BAD_REQUEST)
        #get the file from the request
        file = request.FILES.get("file")
        serializer = ProductSeedingSerializer(data=request.data)
        if serializer.is_valid():
            try:
                #ret will hold the return message and errors in case there was any
                ret = {"details": "Succefully uploaded"}
                #loop through json file
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
                        prod['original_store'] = serializer.data['original_store'].lower()
                        prod['brand'] = prod['brand'].lower()
                        categories = []
                        #check if categorie exist, if not create one
                        for i in [j.strip().lower() for j in serializer.data['categorie'].split(',')]:
                            c = Categorie.objects.filter(categorie_name=i).first()
                            if not c:
                                new_categorie = Categorie(categorie_name=i)
                                new_categorie.save()
                                categories.append(new_categorie.id)
                            else:
                                categories.append(c.id)
                        prod['categorie'] =  categories
                        #check if the data is correct, if so inset it in database
                        prod_serilizer = AddProductSerializer(data=prod)
                        if prod_serilizer.is_valid():
                            prod_serilizer.save()
                    else:
                        #if photo nout found
                        ret[prod['photo']] = "Not found"
                log = Log(user=request.user, action="Added new products succefully")
                log.save()
                return Response(ret, status=status.HTTP_201_CREATED)
            except:
                #if there was an issue
                log = Log(user=request.user, action="Failed to add new products")
                log.save()
                return Response({"details": "json file contains issues"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"details": "Provide a json file"}, status=status.HTTP_400_BAD_REQUEST)


class GetCategoriesView(generics.GenericAPIView):
    """
    get all categories found in database
    """
    serializer_class = CategorieSerializer
    def get(self,request):
        cate = Categorie.objects.all()
        serializer =  CategorieSerializer(cate, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GetBrandsView(generics.GenericAPIView):
    """
    returns all available brands in database, with the amount of products
    """
    serializer_class = BrandSerializer
    def get(self, request):
        query = Product.objects.values('brand').annotate(count=Count('brand')).order_by()
        brands = BrandSerializer(query, many=True)
        return Response(brands.data, status=status.HTTP_200_OK)


class GetStoresView(generics.GenericAPIView):
    """
    returns all available stores in database, with the amount of products
    """
    serializer_class = StoreSerializer
    def get(self, request):
        query = Product.objects.values('original_store').annotate(count=Count('original_store')).order_by()
        stores = StoreSerializer(query, many=True)
        return Response(stores.data, status=status.HTTP_200_OK)


class ProductsView(generics.ListAPIView):
    """
    get products, by categorie name, brand, store, staff_pick, price and id
    it also used for searching
    you can chose sort order by either full_name, -full_name, price, -price, time_added, -time_added
    """
    pagination_class = pagination.PageNumberPagination
    page_size = 50
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    filterset_class = ProductFilter
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['full_name', 'original_store', 'brand', 'description', 'categorie__categorie_name',]
    ordering_fields = ['full_name', 'price', 'time_added']
    ordering = ['-time_added']


class AddOrderView(generics.GenericAPIView):
    """
    Add new order, through the id of the user, and id of products
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    def post(self, request):
        try:
            temp = request.data
            temp['user'] = request.user.id
            print(temp)
            ser = OrderSerializer(data=temp)
            if ser.is_valid():
                ser.save()
                log = Log(action="Added new order", user=request.user)
                log.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response({"details":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"details": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class GetOrderView(generics.GenericAPIView):
    """
    Get order by user id
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GetOrderSerializer
    def get(self, request):
        try:
            query = Order.objects.filter(user=request.user)
            ser = GetOrderSerializer(query, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            return Response({"details": "Not found"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["Delete"])
@permission_classes([IsAuthenticated])
def DeleteOrderView(request, id):
    try:
        obj = Order.objects.get(id=id,user=request.user)
        if obj.status == 'pending':
            obj.status = 'deleted'
            obj.save()
            log = Log(action="Deleted order", user=request.user)
            log.save()
            return Response({"details": "Order deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Can't delete order"}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"details": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
