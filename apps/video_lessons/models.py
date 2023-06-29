from django.db import models


# Create your models here.

class BaseModel(models.Model):
    title = models.CharField()
    video_url = models.CharField()

    class Meta:
        abstract = True


class BasicVideoLessonsModel(BaseModel):
    pass


class FundamentalsMidVideoLessonsModel(BaseModel):
    pass


class FundamentalsFinalVideoLessonsModel(BaseModel):
    pass


class MultidimensionalListsModel(BaseModel):
    pass


class FunctionsAdvancedModel(BaseModel):
    pass


class AdvancedVideoLessonsModel(BaseModel):
    pass


class OOPVideoLessonsModel(BaseModel):
    pass


class JSDOMEventsModel(BaseModel):
    pass


class JSFrontENdVideoLessonsModel(BaseModel):
    pass


class PythonWebVideoLessonsModel(BaseModel):
    pass
