import requests
import json

token = '9ebf617fd4549fd020ab5a31c87bc1f4'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    'name': 'lalalala',
    'photo': 'https://www.freepnglogos.com/uploads/pokemon-png/charmander-pokemon-png-duecant-31.png'
})

'''print(response.text)'''


response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 2702,
    'name': 'hahaha',
    'photo': ''
    })

'''print(response_put.text)'''

response_post = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, 
json={"pokemon_id": "2715"})

'''print(response_post.text)'''