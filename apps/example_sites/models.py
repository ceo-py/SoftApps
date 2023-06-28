from django.db import models

# Create your models here.

from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    site_url = models.URLField()
    code_link = models.URLField()

    class Meta:
        abstract = True


class PythonWebBasicsModel(BaseModel):
    pass


class JSFrontEndModel(BaseModel):
    pass


class JSAdvancedModel(BaseModel):
    pass


class HTMLCSSModel(BaseModel):
    pass


class GamesProjectsModel(BaseModel):
    pass


class DiscordBotsModel(BaseModel):
    pass


class OtherProjectsModel(BaseModel):
    pass


class SuggestionsModel(BaseModel):
    pass


class BooksModel(BaseModel):
    pass


class WebSitesModel(BaseModel):
    pass
