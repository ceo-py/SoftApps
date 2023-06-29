from django.contrib import admin

from apps.discord_bot.models import DiscordBotFeaturesModel

# Register your models here.
admin.site.register((
    DiscordBotFeaturesModel,
))