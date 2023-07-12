from django.urls import path
from index.views import register, index, login, catalogue, about

urlpatterns = [
    path('', index),
    path('register/', register, name='register'),
    path('login/', login),
    path('catalogue/', catalogue),
    path('about', about),
]
