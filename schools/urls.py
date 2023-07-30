from django.urls import path
from schools.views import *

urlpatterns =[
    path('school1/',school1,name='school1'),
    path('school2/',school2,name='school2'),
    path('school3/',school3,name='school3'),

]