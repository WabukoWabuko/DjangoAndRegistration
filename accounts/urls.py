from django.urls import path
from .views import register, login, welcome

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('welcome/<str:email>/', welcome, name='welcome'),
]
