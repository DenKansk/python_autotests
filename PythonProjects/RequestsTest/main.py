import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd314ded3894aa27a3978c472bcf3d5ac'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# Создание покемона

body_create_pokemon = {     # Тело запроса
    "name": "Бульбазавр",
    "photo_id": 12
}

response_create_pokemon = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon) # Запрос
print (response_create_pokemon.text)

pokemon_id = response_create_pokemon.json().get('id') # Извлечь "id" из ответа
print (pokemon_id)

# Смена имени покемона

body_remake_pokemon = {     # Тело запроса
    "pokemon_id": pokemon_id, # Подставить "id" созданного покемона
    "name": "Чермандер",
    "photo_id": 2
}

response_remake_pokemon = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_remake_pokemon)
print (response_remake_pokemon.text)

# Поймать покемона в покебол

body_add_pokeball  = {  # Тело запроса
    "pokemon_id": pokemon_id, # Подставить "id" созданного покемона
}

response_add_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_remake_pokemon)
print (response_add_pokeball.text)