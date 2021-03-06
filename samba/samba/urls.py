"""samba URL Configuration

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
from django.urls import path, include
from danceapp import views as danceapp_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', danceapp_views.index, name='index'),
    # path('', danceapp_views.index, name='index'),
    path('', account_views.tokenCheck, name='index'),
    path('postform/', danceapp_views.postcreate, name='postcreate'),

    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('signup/', account_views.signup, name='signup'),

    path('kakaoLoginLogic/', account_views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', account_views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', account_views.kakaoLogout),

    path('accounts/', include('allauth.urls')),
    # path('google/', include('allauth.urls')),
]
