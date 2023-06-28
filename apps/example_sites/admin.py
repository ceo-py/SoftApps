from django.contrib import admin

from apps.example_sites.models import PythonWebBasicsModel, JSFrontEndModel, JSAdvancedModel, HTMLCSS

# Register your models here.


admin.site.register(PythonWebBasicsModel)
admin.site.register(JSFrontEndModel)
admin.site.register(JSAdvancedModel)
admin.site.register(HTMLCSS)

