from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('form/', views.form, name= 'form'),
    path('resp/', views.respform, name= 'resp')
]