from django.db import models


# Create your models here.

class BaseModel(models.Model):
    command = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    data_type = models.CharField(max_length=10)
    image_url = models.URLField()

    class Meta:
        abstract = True


class DiscordBotFeaturesModel(BaseModel):
    pass
