from django.urls import path
from . import views


urlpatterns = [
    path('', views.classapp, name='class'),
    path('list/', views.class_list, name='class_list'),
    path('write/', views.class_write, name='class_write'),
]