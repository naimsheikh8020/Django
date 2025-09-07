from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("Hello World! I am Home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("MY about Page.")
    return render(request, 'about.html')