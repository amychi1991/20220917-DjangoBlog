"""
DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

#from django.conf.urls import include,url
#import blog.views


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('account/',include('account.urls',namespace='account')),

   #url(r'^$', blog.views.index, name='index'),
   #url(r'^home$', blog.views.index, name='home'),
]
