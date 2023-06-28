from django.shortcuts import render


# Create your views here.
def basic_module(request):
    return render(request, 'basic/python-basic.html')
