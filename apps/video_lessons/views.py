from django.shortcuts import render

from apps.functionality.items import get_all_items
from apps.video_lessons.models import *


# Create your views here.


def youtube_lessons(request):
    advanced_exam_prep = get_all_items(AdvancedVideoLessonsModel)
    oop_exam_prep = get_all_items(OOPVideoLessonsModel)
    context = {
        "basic_exam_prep": get_all_items(BasicVideoLessonsModel),
        "fundamentals_mid_exam_prep": get_all_items(FundamentalsMidVideoLessonsModel),
        "fundamentals_final_exam_prep": get_all_items(
            FundamentalsFinalVideoLessonsModel
        ),
        "multidimensional_lists_prep": get_all_items(MultidimensionalListsModel),
        "functions_advanced_prep": get_all_items(FunctionsAdvancedModel),
        "advanced_exam_prep_p1": advanced_exam_prep[:7],
        "advanced_exam_prep_p2": advanced_exam_prep[7:],
        "oop_exam_prep_p1": oop_exam_prep[:5],
        "oop_exam_prep_p2": oop_exam_prep[5:],
        "js_dom_events_prep": get_all_items(JSDOMEventsModel),
        "js_front_end_exam_prep": get_all_items(JSFrontENdVideoLessonsModel),
        "python_web_exam_prep": get_all_items(PythonWebVideoLessonsModel),
    }

    return render(request, "video_lessons/youtube_lessons.html", context=context)
