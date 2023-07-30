from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def family(request):
    return HttpResponse("<h1>i love my family</h1>")

def members(request):
    return HttpResponse("<marquee><h1>There are five members in my family</h1></marquee>")