from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('contact/', views.contact, name='contact'),
]