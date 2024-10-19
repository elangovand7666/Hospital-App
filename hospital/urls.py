"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('admit/', views.admit, name='admit'),
    path('discharge/',views.discharge,name='discharge'),
    path('bill/',views.bill,name='bill'),
    path('visit/',views.visit,name='visit'),
    path('lss/',views.lss,name='lss'),
    path('lss1/',views.lss1,name='lss1'),
    path('lss3',views.lss3,name='lss3'),
    path('lss2/',views.lss2,name='lss2'),
]
