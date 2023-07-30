from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trees(request):
    return HttpResponse("<h1>i love beautiful trees</h1>")
def monkeys(request):
    return HttpResponse("<h1>monkeys voice always like grooo grooo</h1>")