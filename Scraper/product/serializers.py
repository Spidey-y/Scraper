from rest_framework import serializers, exceptions
from .models import Product, Categorie, Order


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'categorie_name']


class ProductSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'full_name', 'photo', 'price', 'original_link', 'original_store', 'brand', 'staff_pick', 'description', 'categorie', 'time_added']


class ProductSeedingSerializer(serializers.Serializer):
    file = serializers.FileField(required=True, write_only=True, allow_empty_file=False,)
    original_store = serializers.CharField(max_length=255, allow_blank=False, required=True)
    categorie = serializers.CharField(max_length=255, allow_blank=False, required=True)

    def validate_file(self, file):
        if file.content_type != 'application/json':
            raise exceptions.ValidationError('Only json files accepted')
        return file


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['products']


class BrandSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ['brand', 'count']


class StoreSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ['original_store', 'count']


class GetOrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Order
        fields = ['id','products', 'status']


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'full_name', 'photo', 'price', 'original_link', 'original_store', 'brand', 'staff_pick', 'description', 'categorie', 'time_added']
