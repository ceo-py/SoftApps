from django.shortcuts import render

from apps.common.models import BaseModelIndex
from apps.functionality.items import get_all_items


# Create your views here.

def index(request):
    context = {'items': get_all_items(BaseModelIndex)}
    return render(request, 'common/index.html', context=context)
