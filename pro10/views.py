from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<marquee><h1>hello world<h1></marquee>")
def nature(request):
    return HttpResponse("<marquee><h1>i love beautiful nature</h1></marquee>")