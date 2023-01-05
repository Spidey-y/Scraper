from django.db import models


# Create your models here.
class Setting(models.Model):
    phone_number = models.CharField(blank=False, max_length=13)
    email = models.EmailField(blank=False)
    address = models.CharField(blank=False, max_length=255,)
    google_map_link = models.CharField(blank=False, max_length=1000, help_text="address (google map link)")
    about_us_1 = models.TextField(blank=False, help_text="left side")
    about_us_2 = models.TextField(blank=False, help_text="center")
    about_us_2 = models.TextField(blank=False, help_text="right side")

    def __str__(self):
        return "About us settings"
