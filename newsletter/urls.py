from django.contrib import admin
from django.urls import path
from newsletter import views

urlpatterns = [
    path("", views.index, name='home'),
    path("select", views.select, name='Select'),
    path("post", views.post, name='Post'),
    
]
