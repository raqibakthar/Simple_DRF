from django.urls import path
from home.views import index,person,login

urlpatterns = [

    path('index/',index),
    path('people/',person),
    path('login/',login),
    
]
