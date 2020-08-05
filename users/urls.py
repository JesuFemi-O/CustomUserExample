from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name= 'home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register')
]