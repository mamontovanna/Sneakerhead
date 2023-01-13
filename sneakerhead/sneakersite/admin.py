from django.contrib import admin
from .models import jordan
from .models import *
from django.db import models

class JordanAdmin(admin.ModelAdmin):
    list_display = ['Название', 'Цена', 'Описание', '38', '39', '40', '41', '42', '43', '44', '45', 'Изображение']
class Nike(admin.ModelAdmin):
    list_display = ('Название', 'Цена', 'Описание', '38', '39', '40', '41', '42', '43', '44', '45', 'Изображение',)
class Adidas(admin.ModelAdmin):
    list_display = ('Название', 'Цена', 'Описание', '38', '39', '40', '41', '42', '43', '44', '45', 'Изображение')

# Register your models here.
admin.site.register(jordan)
admin.site.register(nike)
admin.site.register(adidas)
admin.site.register(guest)
admin.site.register(cart_model)

