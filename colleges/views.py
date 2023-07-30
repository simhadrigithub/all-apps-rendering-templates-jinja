from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def college1(request):
    return render(request,'college1.html')
def college2(request):
    return render(request,'college2.html')

def college3(request):
    return HttpResponse("<marquee><h1>i hope you gauys those are understanding which iam telling with you all topics about the school information</h1></marquee>")
