from django.urls import path
from app4.views import *

urlpatterns =[
    path('father/',father,name='father'),
    path('mother/',mother,name='mother'),
]