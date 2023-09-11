from django.shortcuts import render

from apps.example_sites.models import *
from apps.functionality.items import get_all_items


# Create your views here.


def example_sites(request):
    return render(
        request,
        "example_sites/web-examples.html",
        context={
            "web_items": get_all_items(PythonWebBasicsModel),
            "js_front_end": get_all_items(JSFrontEndModel),
            "js_advanced": get_all_items(JSAdvancedModel),
            "html_css": get_all_items(HTMLCSSModel),
            "games": get_all_items(GamesProjectsModel),
            "discord_bots": get_all_items(DiscordBotsModel),
            "other_projects": get_all_items(OtherProjectsModel),
            "suggestions": get_all_items(SuggestionsModel),
            "books": get_all_items(BooksModel),
            "web_sites": get_all_items(WebSitesModel),
            "react_items": get_all_items(ReactAppModel),
        },
    )


def post_task(request):
    return render(request, "example_sites/post-task.html")


def sprint_planning(request):
    return render(request, "example_sites/sprint_planning.html")


def scary_story(request):
    return render(request, "example_sites/scary-story.html")


def music_site(request):
    return render(request, "example_sites/music_site.html")


def hotel_reservation(request):
    return render(request, "example_sites/hotel-reservation.html")


def ski_lift(request):
    return render(request, "example_sites/ski-lift.html")


def travel_agency(request):
    return render(request, "example_sites/travel_agency.html")


def service(request):
    return render(request, "example_sites/service.html")


def payment_plan(request):
    return render(request, "example_sites/payment-plan.html")


def photography_portfolio(request):
    return render(request, "example_sites/photography_portfolio.html")


def animal_help(request):
    return render(request, "example_sites/animal_help.html")


def fees(request):
    return render(request, "example_sites/fees.html")
