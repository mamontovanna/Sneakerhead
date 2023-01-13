from django.shortcuts import render
from sneakersite.models import *
from django.contrib.auth import authenticate
from django.http import HttpResponse#вывод чего-то
from django.contrib.auth.models import User

def main(request):
    return render(request, 'main_page.html')

def auth(request):
    if request.method=="POST":
        data=request.POST
        user=authenticate(username=data["name"], password=data["pas"])
        if user:
            request.session['test']="test"
            return render(request, 'main_page.html')
        else:
            return HttpResponse("Пользователь не авторизован. Неверное имя пользователя или пароль!")
    return render(request, 'auth.html')

def register(request):
    if request.method=="POST":
        data=request.POST
        new=User.objects.create_user( username = data["name"], last_name=data["surn"],email=data["email"], password= data["pas"])
        new.save()
        request.session['test']="test"
        return render(request, 'main_page.html')
    return render(request, 'registration.html')

def jordan_view(request):
    data=jordan.objects.all()
    return render(request, 'jordan.html', {"cards":data})
def jordan_card(request, post_id):
    if request.method=="GET":
        data=jordan.objects.filter(id=post_id)
        
        return render(request, 'jordan_card.html',{"dat":data})

def Nike(request):
    data=nike.objects.all()
    return render(request, 'nike.html', {"cards":data})
def nike_card(request, post_id):
   if request.method=="GET":
        data=nike.objects.filter(id=post_id)
        return render(request, 'nike_card.html',{"dat":data})

def Adidas(request):
    data=adidas.objects.all()
    return render(request, 'adidas.html', {"cards":data})
def adidas_card(request, post_id):
   if request.method=="GET":
        data=adidas.objects.filter(id=post_id)
        return render(request, 'adidas_card.html',{"dat":data})

def cart_view(request):
    return render(request,'cart.html')
    #return render(request, 'nike_card.html')
# Create your views here.
