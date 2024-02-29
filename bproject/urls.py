"""
URL configuration for bproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from bapp import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('index/',views.index),
   
    path('login/',views.Login), 
    path('register/',views.Register),
    path('shopreg/',views.shopreg),
    path('rescommon/',views.rescommon),
    path('addproduct/',views.addproduct),
    path('editpro/',views.editproduct),
    path('viewpro/',views.viewpro),
    path('delet/',views.delet),
    path('shopview/',views.shopview),
    # path('rdelete/',views.rdelet)
    path('cview/',views.cview)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
