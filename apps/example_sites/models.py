from django.db import models


# Create your models here.


class PythonWebBasicsModel(models.Model):
    title = models.CharField(

    )

    image_url = models.URLField(

    )

    site_url = models.URLField(

    )

    code_link = models.URLField(

    )


class JSFrontEndModel(models.Model):
    title = models.CharField(

    )

    image_url = models.URLField(

    )

    site_url = models.URLField(

    )

    code_link = models.URLField(

    )


class JSAdvancedModel(models.Model):
    title = models.CharField(

    )

    image_url = models.URLField(

    )

    site_url = models.URLField(

    )

    code_link = models.URLField(

    )


class HTMLCSS(models.Model):
    title = models.CharField(

    )

    image_url = models.URLField(

    )

    site_url = models.URLField(

    )

    code_link = models.URLField(

    )
