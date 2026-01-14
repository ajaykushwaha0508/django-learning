from django.urls import path
from .views import *

urlpatterns=[
    path('helloWorld/' , helloWorld),
    path('home/' , home),
    path('home/<int:id>/' ,getContent ,name="posts"),
    path('blog' ,blog),
    path('about' , about)
    
]