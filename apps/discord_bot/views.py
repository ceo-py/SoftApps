from django.shortcuts import render

from apps.discord_bot.models import DiscordBotFeaturesModel
from apps.functionality.items import get_all_items


# Create your views here.

def discord_bot(request):
    all_items = get_all_items(DiscordBotFeaturesModel)
    context = {
        'key_features': all_items[:8],
        'lang_specific_features': all_items[8:],
        'all_commands': all_items
    }
    return render(request, 'discord_bot/discord-bot.html', context=context)

