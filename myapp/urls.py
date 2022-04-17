from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('checkout', checkout, name="checkout"),
    path('add_product_to_basket/<str:product_id>/',
         add_product_to_basket, name="add_to_basket"),
    path('remove_product_from_basket/<str:product_id>/',
         remove_product_from_basket, name="remove_product_from_basket"),

]
