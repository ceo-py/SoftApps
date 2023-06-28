from django.urls import path

from apps.example_sites.views import example_sites, post_task, sprint_planning, scary_story,music_site

urlpatterns = [
    path("", example_sites, name="example_sites"),
    path("PostTask", post_task, name="post_task"),
    path("SprintPlanning", sprint_planning, name="sprint_planning"),
    path("ScaryStory", scary_story, name="scary_story"),
    path("MusicSite", music_site, name="music_site"),
]
