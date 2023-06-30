from django.urls import path

from apps.discord_bot.views import discord_bot

urlpatterns = [
    path("", discord_bot, name="discord_bot"),
]
