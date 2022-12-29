from rest_framework import generics
from .models import Ad
from rest_framework import serializers


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'photo', 'is_active', 'position']


class AdsView(generics.ListAPIView):
    serializer_class = AdsSerializer
    queryset = Ad.objects.filter(is_active=True)
