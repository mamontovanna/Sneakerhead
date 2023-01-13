"""sneakerhead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from sneakerhead import settings
from django.contrib import admin
from django.urls import path
from sneakersite.views import main
from sneakersite.views import auth
from sneakersite.views import register
from sneakersite.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('auth/', auth),
    path('reg/', register),
    path('jordan/', jordan_view),
    path('nike/', Nike),
    path('adidas/', Adidas),
    path('nike/<int:post_id>', nike_card),
    path('jordan/<int:post_id>', jordan_card),
    path('adidas/<int:post_id>', adidas_card),
    path('cart/', cart_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
