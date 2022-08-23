"""expenseTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from TrackingApp import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', v1.home),
    path('signup', v1.signup),
    path('login', v1.login),
    path('Dashboard', v1.Dashboard),
    path('RegisterUser', v1.RegisterUser),
    path('CheckloginUser', v1.CheckloginUser),
    path('master', v1.master),
    path('SaveIncome', v1.SaveIncome),
    path('RenderIncome', v1.RenderIncome),
    path('ShowIncome', v1.ShowIncome),
    path('RenderExpense', v1.RenderExpense),
    path('SaveExpense', v1.SaveExpense),
    path('ShowExpense', v1.ShowExpense),
    path('allTransaction', v1.allTransaction),
]
