from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class guest(models.Model):
    name=models.CharField(max_length=50, verbose_name="Имя")
    surname=models.CharField(max_length=50, verbose_name="Фамилия")
    email=models.EmailField(max_length=254, verbose_name="Адрес электронной почты")
    phone=models.CharField(max_length=20, verbose_name="Телефон")
    login=models.CharField(max_length=100, verbose_name="Логин")
    password=models.CharField(max_length=100, verbose_name="Пароль")

class jordan(models.Model):
    name=models.CharField(max_length=200, verbose_name="Название модели")
    cost=models.PositiveSmallIntegerField(verbose_name="Цена")
    description=models.TextField(max_length=2000, verbose_name='Описание')
    size38=models.BooleanField(verbose_name="38")
    size39=models.BooleanField(verbose_name="39")
    size40=models.BooleanField(verbose_name="40")
    size41=models.BooleanField(verbose_name="41")
    size42=models.BooleanField(verbose_name="42")
    size43=models.BooleanField(verbose_name="43")
    size44=models.BooleanField(verbose_name="44")
    size45=models.BooleanField(verbose_name="45")
    image=models.ImageField(upload_to="images/jordan/", blank=True, verbose_name='Изображение')
    def __str__(self):
        return self.name

class nike(models.Model):
    name=models.CharField(max_length=200, verbose_name="Название модели")
    cost=models.PositiveSmallIntegerField(verbose_name="Цена")
    description=models.TextField(max_length=2000, verbose_name='Описание')
    size38=models.BooleanField(verbose_name="38")
    size39=models.BooleanField(verbose_name="39")
    size40=models.BooleanField(verbose_name="40")
    size41=models.BooleanField(verbose_name="41")
    size42=models.BooleanField(verbose_name="42")
    size43=models.BooleanField(verbose_name="43")
    size44=models.BooleanField(verbose_name="44")
    size45=models.BooleanField(verbose_name="45")
    image=models.ImageField(upload_to="images/nike/", blank=True, verbose_name='Изображение')
    def __str__(self):
        return self.name

class adidas(models.Model):
    name=models.CharField(max_length=200, verbose_name="Название модели")
    cost=models.PositiveSmallIntegerField(verbose_name="Цена")
    description=models.TextField(max_length=2000, verbose_name='Описание')
    size38=models.BooleanField(verbose_name="38")
    size39=models.BooleanField(verbose_name="39")
    size40=models.BooleanField(verbose_name="40")
    size41=models.BooleanField(verbose_name="41")
    size42=models.BooleanField(verbose_name="42")
    size43=models.BooleanField(verbose_name="43")
    size44=models.BooleanField(verbose_name="44")
    size45=models.BooleanField(verbose_name="45")
    image=models.ImageField(upload_to="images/adidas/", blank=True, verbose_name='Изображение')
    def __str__(self):
        return self.name
    
class cart_model(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    sneakerid=models.ForeignKey(nike, on_delete=models.CASCADE)

    def cart_add(userid, sneakerid, self):
        cart=cart_model(sneakerid_id=sneakerid, userid_id=userid)
        cart.save()

    
