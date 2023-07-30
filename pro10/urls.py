"""
URL configuration for pro10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
from app1.views import *
from app2.views import trees,monkeys
import app3,app4
import schools,colleges
import jinja_printing_tags,jinja_operational_tag


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello,name='hello'),
    path('nature/',nature,name='nature'),
    path('family/',family,name='family'),
    path('members/',members,name='members'),
    path('monkeys/',monkeys,name='monkeys'),
    path('trees/',trees,name='trees'),
    path('app3/',include('app3.urls')),
    path('app4/',include('app4.urls')),
    path('schools/',include('schools.urls')),
    path('colleges/',include('colleges.urls')),
    path('jinja_printing_tags/',include('jinja_printing_tags.urls')),
    path('jinja_operational_tag/',include('jinja_operational_tag.urls')),

]
