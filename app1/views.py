from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ramesh(request):
    return HttpResponse('<h1><marquee>This is specific url mapping for</marquee><h1>')


