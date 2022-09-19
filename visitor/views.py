from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('visitor')
    # render(request, 'visitor/home.html')