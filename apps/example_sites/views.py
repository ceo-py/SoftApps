from django.shortcuts import render

from apps.example_sites.models import PythonWebBasicsModel, JSFrontEndModel
from apps.functionality.items import get_all_items


# Create your views here.


def example_sites(request):
    return render(request, 'example_sites/web-examples.html', context={
        'web_items': get_all_items(PythonWebBasicsModel),
        'js_front_end': get_all_items(JSFrontEndModel)
    })


def post_task(request):
    return render(request, 'example_sites/post-task.html')


def sprint_planning(request):
    return render(request, 'example_sites/sprint_planning.html')


def scary_story(request):
    return render(request, 'example_sites/scary-story.html')


def music_site(request):
    return render(request, 'example_sites/music_site.html')
