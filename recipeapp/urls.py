"""recipeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include
from recipes import views as rv
from register import views as v
from shoppinglist import views as sv


urlpatterns = [
    path('recipeboss/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('register/', v.register, name="register"),
    path('user/', include('django.contrib.auth.urls')),
    path('shoppinglist',sv.index, name="shopping_list"),
    path('', rv.home, name="home")
]
