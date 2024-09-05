from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('liste_produit/',views.index,name='listeproduit'),
    path('',views.base,name='base'),
    path('entrer/',views.entrer,name='entrer'),
    path('ajouterproduit/',views.ajouter,name='add')
]