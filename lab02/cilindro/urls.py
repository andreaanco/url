from django.urls import path
from . import views



urlpatterns = [

    path('cilindro/', views.cilindro, name='cilindro'),

    
]
