from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chinna(request):
    return HttpResponse("<marquee><h1>chinna studying 10th class in settipalli</h1></marquee>")

def lavanya(request):
    return HttpResponse("<marquee><h1>lavanya completed 10th class in settipalli(already passout student)</h1></marquee>")