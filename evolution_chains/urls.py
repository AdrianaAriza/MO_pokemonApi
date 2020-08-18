from django.urls import path, include
from .views import ApiPokemon, Index, CreateFamily

urlpatterns = [
    path('api/<str:name>', ApiPokemon.as_view()),
    path('', Index.as_view()),
    path('create-family/<str:id>', CreateFamily.as_view()),
]
