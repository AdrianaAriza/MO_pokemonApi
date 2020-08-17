from django.http import HttpResponse
from rest_framework.views import APIView
from.models import Pokemon
import json


class ApiPokemon(APIView):

    def get(self, request, name):
        try:
            pokemon = Pokemon.objects.get(name=name)
            pokemon.base_stats = json.loads(pokemon.base_stats)
            pre_evolution = Pokemon.objects.filter(evolutions=name)
            pokemon = pokemon.__dict__
            del (pokemon['_state'])
            evolutions_list = pokemon['evolutions'].split(', ')
            print(evolutions_list)
            evolutions = Pokemon.objects.filter(name__in=pokemon['evolutions'].split(', '))
            print(evolutions)
            pokemon['evolutions'] = [
            {
                'name': evolution.name,
                'type': 'evolution',
                'id': evolution.id,
            } for evolution in evolutions
            ]
            print(pokemon['evolutions'])
            if pre_evolution:
                pokemon['evolutions'].append(
                {
                    'name': pre_evolution[0].name,
                    'type': 'pre-evolution',
                    'id': pre_evolution[0].id,
                }
                )
            return HttpResponse(json.dumps(pokemon), content_type='application/json')

        except Pokemon.DoesNotExist:
            return HttpResponse(json.dumps({"name": "pokemon not found"}), content_type='application/json')

