"""Django_xadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.static import serve

from Apps.xadmin_App import views
import xadmin
from Apps.xadmin_App.views import *
from django.conf.urls import include, url

from Django_xadmin.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('article/',views.article),
    path('articlelist/',views.articleList),
    path('test/',test,name='test'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
]





