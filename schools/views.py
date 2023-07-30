from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def school1(request):
    return render(request,'school1.html')

def school2(request):
    return render(request,'school2.html')

def school3(request):
    return HttpResponse("<marquee><h1>i hope you gauys those are understanding which iam telling with you all topics about the school information</h1></marquee>")
