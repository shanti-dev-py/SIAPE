from django.urls import path, include
from . import views

urlpatterns =[
    path('',views.helllo),
    path('about/', views.about),
]