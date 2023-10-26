from django.urls import path

from ActBM import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('crearTablero/', views.creartablero, name='crearTablero'),
]