from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name= 'home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),
    path('api/users/', views.RegistrationAPIView.as_view()),
    path('api/login/', views.LoginAPIView.as_view()),
    path('api/user/', views.UserRetrieveUpdateAPIView.as_view()),
]