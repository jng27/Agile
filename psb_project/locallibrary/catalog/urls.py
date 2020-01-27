from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home/', views.index, name='index'),
    url(r'^newScore/', views.newScore, name='newScore'),
    
]