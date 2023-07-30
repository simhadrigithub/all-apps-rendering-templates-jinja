from django.urls import path
from colleges.views import *

urlpatterns =[
    path('college1/',college1,name='college1'),
    path('college2/',college2,name='college2'),
    path('college3/',college3,name='college3'),
    
    
]