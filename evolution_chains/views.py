import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from.models import Pokemon

class Index (APIView):
    def get(self, request):
        return render(request, 'index.html')

class ApiPokemon(APIView):
    def get(self, request, name):
        try:
            pokemon = Pokemon.objects.get(name=name.lower())
            pokemon.base_stats = json.loads(pokemon.base_stats)
            pre_evolution = Pokemon.objects.filter(evolutions__contains=name)
            pokemon = pokemon.__dict__
            del (pokemon['_state'])
            if pokemon['evolutions']:
                evolutions_list = pokemon['evolutions'].split(', ')
            else:
                evolutions_list = []
            evolutions = Pokemon.objects.filter(name__in=evolutions_list)
            pokemon['evolutions'] = [
                {
                    'name': evolution.name,
                    'evolutionType': 'evolution',
                    'id': evolution.id,
                    'image': evolution.image,
                } for evolution in evolutions
            ]
            if pre_evolution:
                pokemon['evolutions'].append(
                    {
                        'name': pre_evolution[0].name,
                        'evolutionType': 'pre-evolution',
                        'id': pre_evolution[0].id,
                        'image': pre_evolution[0].image,
                    }
                )
            return HttpResponse(json.dumps(pokemon), content_type='application/json')

        except Pokemon.DoesNotExist:
            return HttpResponse(json.dumps({"name": "pokemon not found"}), content_type='application/json')

class CreateFamily(APIView):
    def get(self, request, id):
        os.system(f'python manage.py evolution_chains {id}')
        return HttpResponse(json.dumps({"status": "family tree created"}), content_type='application/json')

