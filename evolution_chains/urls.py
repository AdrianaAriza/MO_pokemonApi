from django.urls import path, include
from .views import ApiPokemon, Index

urlpatterns = [
    path('api/<str:name>', ApiPokemon.as_view()),
    path('', Index.as_view())
]
