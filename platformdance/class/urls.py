from django.urls import path
from . import views


urlpatterns = [
    path('', views.classapp, name='class')
]