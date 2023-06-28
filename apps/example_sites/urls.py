from django.urls import path

from apps.example_sites.views import example_sites, post_task, sprint_planning, scary_story, music_site, \
    hotel_reservation, ski_lift, travel_agency, service, payment_plan, photography_portfolio, animal_help, \
    fees

urlpatterns = [
    path("", example_sites, name="example_sites"),
    path("PostTask", post_task, name="post_task"),
    path("SprintPlanning", sprint_planning, name="sprint_planning"),
    path("ScaryStory", scary_story, name="scary_story"),
    path("MusicSite", music_site, name="music_site"),
    path("Hotel", hotel_reservation, name="hotel_reservation"),
    path("SkiLift", ski_lift, name="ski_lift"),
    path("TravelAgency", travel_agency, name="travel_agency"),
    path("Service", service, name="service"),
    path("PaymentPlan", payment_plan, name="payment_plan"),
    path("PhotographyPortfolio", photography_portfolio, name="photography_portfolio"),
    path("AnimalHelp", animal_help, name="animal_help"),
    path("Fees", fees, name="fees"),
]
