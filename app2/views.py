from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rupesh(request):
    return HttpResponse('<h1><marquee>This is specific url mapping for app2</marquee><h1>')