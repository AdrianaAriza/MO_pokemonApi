# POKEDEX

https://mopokemonapi.herokuapp.com/

## Description

This project is the technical test for the position of BackEnd developer in MOTECNOLOGIAS

Requiriments:

- Build a Command that receives as its only parameter an ID, to fill a database.
- Expose a Web Service which only parameter is the “name” of a Pokemon
  search. This service must not do a request towards the PokeApi. The
  response must include the following information:
- Pokemon details available
  - Include for all the evolutions related
  - Evolution type (Preevolution / Evolution)
  - Id
  - Name

## How to used the Web App📦

Go to: https://mopokemonapi.herokuapp.com/

Enter the name of the pokemon you want to get information, if the name does not match with any of the pokemons in the database you will get a "POKEMON NOT FOUND" warming, it means that pokemon have not added to the database yet.

You can add pokemons to the database adding its family, so below the warming you will find a input, write there the number id of the pokemon's family tree and click "enviar". Now you can check again by the name of your pokemon and you will get of its information.

Please report any issue or improvement to a-d-r-u@hotmail.com.

## How to used the Project locally 🔧

1. Clone the reposiroty:

   `git clone https://github.com/AdrianaAriza/MO_pokemonApi.git`

2. Go to project folder:

   `cd MO_pokemonApi`

3. Create a virtual environment and activate it:

   `python -m venv <name_env>`
   `source <name_env>/bin/activate`

4. Install requirements:

   `pip install -r requirements.txt`

5. Set local database:

   1. Go to the /MO_pokemonApi/MO_test/settings.py files
   2. Comment the Deployed Database settings and uncomment the Local Database settings

6. Run Migrations:

   Execute:
   `python manage.py migrate`

7. Set estatic files:

   Execute:
   `python manage.py collectstatic`

8. Fill the Database out - Add Family Trees :

   The way to fill the database is through the command "evolution_chains". It creates on the database all the pokemons who belongs a family according to the given id:

   Execute:
   `python manage.py evolution_chains <id-family>`

   Where id-family is an integer, example:
   `python manage.py evolution_chains 8`

9. Run server:

   Execute:
   `python manage.py runserver`

10. Request the service:

- http://localhost:8000/api/"pokemon-name"
- http://localhost:8000/create-family/"family-id"

## Deployment 📦

- [Python 3](https://www.python.org/) - backend
- [Djando](https://www.djangoproject.com/) - framework
- [PostgresSql](https://www.postgresql.org/) - DataBase
- [Heroku](www.heroku.com) - Deploy
- [HTLM CSS JS]() - frontend

## Author ✒️

- [Adriana Ariza](https://www.linkedin.com/in/laab/)
