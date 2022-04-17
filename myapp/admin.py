from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(MyBasket)
admin.site.register(MyBasket_Product)
