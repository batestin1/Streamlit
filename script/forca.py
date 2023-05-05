#!/usr/local/bin/python3

###################################################################################################
#                                                                                                 #
# SCRIPT FILE: forca.py                                                                           #
# CREATION DATE: 02/02/2023                                                                       #
# HOUR: 10:10                                                                                     #
# DISTRIBUTION USED: UBUNTU                                                                       #
# OPERATIONAL SYSTEM: LINUX                                                                       #
#                                                                             DEVELOPED BY: BATES #
###################################################################################################
#                                                                                                 #
# SUMMARY: Jogo da Forca                                                                          #
#                                                                                                 #
###################################################################################################

import streamlit as st
import requests
import random
import json

with open('param/param.json') as f:
    keys = json.load(f)

image = keys['icon']
logo = keys['logo']
api = keys['api']
api_content = keys['api_content']
MAX_ATTEMPTS = 2

pokemon_list = requests.get(api).json()['results']

def get_pokemon_info(pokemon_id):
    pokemon = requests.get(f'{api_content}{pokemon_id}').json()
    name = pokemon['name'].capitalize()
    abilities = ', '.join([ability['ability']['name'].capitalize() for ability in pokemon['abilities']])
    moves = ', '.join([move['move']['name'].capitalize() for move in pokemon['moves']])
    image_url = pokemon['sprites']['front_default']
    return name, abilities, moves, image_url

def play_game():
    st.title('QUE POKÉMON É ESSE?')
    pokemon_id = st.session_state.get('pokemon_id', 1)
    name, abilities, moves, image_url = get_pokemon_info(pokemon_id)
    display_name = ' '.join(['_' if c.isalpha() else c for c in name])
    guess = st.text_input('Adivinhe o Pokémon', value=display_name, key='Adivinhe')
    if st.button('Submit'):
        if guess.lower() == name.lower():
            st.success('Parabéns! Você venceu!')
            st.image(image_url, caption=name, width=150)
            st.write('Nome:', name)
            st.write('Habilidades:', abilities)
            st.write('Poderes:', moves)
            pokemon_id = (pokemon_id + 1) % len(pokemon_list)
            name, abilities, moves, image_url = get_pokemon_info(pokemon_id)
            display_name = ' '.join(['_' if c.isalpha() else c for c in name])
            st.session_state['pokemon_id'] = pokemon_id
            st.session_state['hints'] = ['abilities', 'moves']
        else:
            global MAX_ATTEMPTS
            MAX_ATTEMPTS -= 1
            if MAX_ATTEMPTS == 0:
                st.error('GAME OVER')
                st.session_state['pokemon_id'] = 1
                st.session_state['hints'] = ['abilities', 'moves']
                MAX_ATTEMPTS = 3
            else:
                st.warning(f'Errado! Você tem {MAX_ATTEMPTS} tentativas.')
    if st.button('Dicas'):
        hints = st.session_state.get('hints', [])
        if hints:
            hint_key = random.choice(hints)
            hint_value = eval(hint_key)
            st.info(f'O Pokémon tem {hint_key}: {hint_value}')
            hints.remove(hint_key)
            st.session_state['hints'] = hints
        else:
            st.warning('Você usou todas as dicas.')

if __name__ == '__main__':
    play_game()
