from django.urls import path
from .views import AboutUsView


urlpatterns = [
    path('', AboutUsView)
]