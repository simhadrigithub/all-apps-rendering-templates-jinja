from django.urls import path
from jinja_operational_tag.views import *

urlpatterns =[
    path('jinja_operational/',jinja_operational,name='jinja_operational'),
    
]