from django.urls import path, include
from .views import ApiPokemon

urlpatterns = [
    path('api/<str:name>', ApiPokemon.as_view())
]
