from django.contrib import admin

from apps.example_sites.models import *

# Register your models here.

admin.site.register((
    PythonWebBasicsModel,
    JSFrontEndModel,
    JSAdvancedModel,
    HTMLCSSModel,
    GamesProjectsModel,
    DiscordBotsModel,
    OtherProjectsModel,
    SuggestionsModel,
    BooksModel,
    WebSitesModel

))
