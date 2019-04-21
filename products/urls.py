from django.urls import path
from . import views

#/products-which is the root of the app
#for eg/products/new or /products/trending
urlpatterns=[
    path('', views.index),
]
