from django.urls import path

from apps.video_lessons.views import youtube_lessons

urlpatterns = [
    path("VideoLessons/", youtube_lessons, name="youtube_lessons"),
]
