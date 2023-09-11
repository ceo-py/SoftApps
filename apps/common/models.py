from django.db import models


# Create your models here.

class BaseModelIndex(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    button_text = models.CharField(max_length=50)
    url_page_to_link = models.CharField(max_length=50)

