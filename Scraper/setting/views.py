from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .models import Setting


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            'phone_number',
            'email',
            'address',
            'google_map_link',
            'about_us_1',
            'about_us_2',
            'about_us_2',
        ]


@swagger_auto_schema(method='GET',)
@api_view(["GET"])
def AboutUsView(request):
    """
    Returns content for about us and contact us page
    """
    info = Setting.objects.all().first()
    info = AboutUsSerializer(info)
    return Response(info.data, status=status.HTTP_200_OK)


