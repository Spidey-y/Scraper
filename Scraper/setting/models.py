from django.db import models


# Create your models here.
class Setting(models.Model):
    phone_number = models.CharField(blank=False, max_length=13)
    email = models.EmailField(blank=False)
    address = models.CharField(blank=False, max_length=255,)
    google_map_link = models.CharField(blank=False, max_length=1000, help_text="address (google map link)")
    about_us = models.TextField(blank=False)

    def __str__(self):
        return "About us settings"
