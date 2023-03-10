from django.urls import path
from . import views

urlpatterns = [
    #initialize server
    path('', views.getServer),
]
