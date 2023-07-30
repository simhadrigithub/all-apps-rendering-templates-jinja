from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def father(request):
    return HttpResponse("<marquee><h1>father is very hardworker and he holds his family responsibilities</marquee></h1>")

def mother(request):
    return HttpResponse("<marquee><h1>mother is father wife and her holds his family responsibilities</marquee></h1>")