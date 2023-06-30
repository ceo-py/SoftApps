from django.contrib import admin

from apps.example_sites.models import *
from apps.video_lessons.models import *

# Register your models here.

admin.site.register(
    (
        PythonWebBasicsModel,
        JSFrontEndModel,
        JSAdvancedModel,
        HTMLCSSModel,
        GamesProjectsModel,
        DiscordBotsModel,
        OtherProjectsModel,
        SuggestionsModel,
        BooksModel,
        WebSitesModel,
        BasicVideoLessonsModel,
        FundamentalsMidVideoLessonsModel,
        FundamentalsFinalVideoLessonsModel,
        MultidimensionalListsModel,
        FunctionsAdvancedModel,
        AdvancedVideoLessonsModel,
        OOPVideoLessonsModel,
        JSDOMEventsModel,
        JSFrontENdVideoLessonsModel,
        PythonWebVideoLessonsModel,
    )
)
