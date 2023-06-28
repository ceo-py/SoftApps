from django.contrib import admin

from apps.example_sites.models import PythonWebBasicsModel, JSFrontEndModel

# Register your models here.


admin.site.register(PythonWebBasicsModel)
admin.site.register(JSFrontEndModel)

