from django.urls import path
from jinja_printing_tags.views import *

urlpatterns =[
    path('jinja_printing/',jinja_printing,name='jinja_printing'),
]