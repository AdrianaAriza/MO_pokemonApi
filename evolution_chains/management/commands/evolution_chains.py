from django.core.management.base import BaseCommand
from evolution_chains.models import Pokemon
import requests
import json


class Command(BaseCommand):
    help = 'Evolution chains are essentially family tree'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='The identifier for this resource')

    @staticmethod
    def get_evolves_to(evolution_list):
        evolution_names = []
        for evolution in evolution_list:
            if 'species' in evolution:
                evolution_names.append(evolution['species']['name'])
        if len(evolution_list) == 0:
            return None
        return ', '.join(evolution_names)

    @staticmethod
    def get_base_stats(stats):
        base_stats = {}
        for stat in stats:
            base_stats[stat['stat']['name']] = stat['base_stat']
        return base_stats

    def save_pokemon(self, name, family_step):
        # make pokemon request
        re = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')

        # validate request
        if re.status_code == 200:
            re = json.loads(re.text)
            evolutions = self.get_evolves_to(family_step['evolves_to'])
            base_stats = self.get_base_stats(re['stats'])
            data = {'name': name, 'height': re['height'], 'weight': re['weight'], 'id': re['id'],
                    'evolutions': evolutions, 'base_stats': json.dumps(base_stats),
                    'image': re['sprites']['other']['dream_world']['front_default']}
            # save Pokemon in db
            Pokemon.objects.update_or_create(id=data['id'], name=data['name'], defaults=data)

            # validate if have evolution
            if evolutions:
                for evolution in family_step['evolves_to']:
                    if 'species' in evolution:
                        self.save_pokemon(evolution['species']['name'], evolution)

    def handle(self, *args, **kwargs):
        evolution_id = kwargs['id']

        # make evolution-chain request
        response = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{evolution_id}/')

        # validate response
        if response.status_code != 200:
            self.stdout.write(f"Evolution chains {evolution_id} doesn't exist")
            return
        response = json.loads(response.text)['chain']

        if 'species' in response and 'name' in response['species']:
            self.save_pokemon(response['species']['name'], response)

        self.stdout.write(f"Members of family trees were saved")
