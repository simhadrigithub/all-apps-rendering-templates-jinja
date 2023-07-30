from django.urls import path
from app3.views import *

urlpatterns =[
    path('chinna/',chinna,name='chinna'),
    path('lavanya/',lavanya,name='lavanya'),


]