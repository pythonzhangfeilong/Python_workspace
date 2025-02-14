"""Django_BackstageStyle URL Configuration

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
# from django.contrib import admin
# from django.urls import path
# import xadmin
# urlpatterns = [
#     path('xadmin/', xadmin.site.urls),
# ]
from django.conf.urls import include, url
from django.contrib import admin
from Stayle_App.views import index
urlpatterns = [

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	# 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT，对应上面的media
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT })
