#!/usr/local/bin/python3

###################################################################################################
#                                                                                                 #
# SCRIPT FILE: pokeapi.py                                                                         #
# CREATION DATE: 02/02/2023                                                                       #
# HOUR: 10:10                                                                                     #
# DISTRIBUTION USED: UBUNTU                                                                       #
# OPERATIONAL SYSTEM: LINUX                                                                       #
#                                                                             DEVELOPED BY: BATES #
###################################################################################################
#                                                                                                 #
# SUMMARY: Poke api                                                                               #
#                                                                                                 #
###################################################################################################

import requests
import streamlit as st
from PIL import Image
import os
import json

with open('param/param.json') as f:
    keys = json.load(f)

image = keys['icon']
logo = keys['logo']
api = keys['api']
api_content = keys['api_content']

os.environ["STREAMLIT_DEBUG"] = "1"



# Define a função para buscar os dados do Pokémon
def get_pokemon_data(pokemon_name):
    url = f"{api_content}{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Não foi possível encontrar o Pokémon")

# Define a função para exibir as informações do Pokémon
def show_pokemon_info(pokemon_name):
    data = get_pokemon_data(pokemon_name)

    # Define o layout da imagem e das informações
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(data['sprites']['other']['official-artwork']['front_default'], width=200)
    with col2:
        st.write(f"<h1 style='text-align: center'>{data['name'].capitalize()}</h1>", unsafe_allow_html=True)
        st.write(f"<h4>Pokédex: {data['id']}</h4>", unsafe_allow_html=True)
        st.write(f"<h4>Tipo: {', '.join([t['type']['name'].capitalize() for t in data['types']])}</h4>", unsafe_allow_html=True)
        st.write(f"<h4>Poderes: {', '.join([move['move']['name'].capitalize() for move in data['moves'][:5]])}</h4>", unsafe_allow_html=True)
        st.write(f"<h4>Nível de ataque: {data['stats'][1]['base_stat']}</h4>", unsafe_allow_html=True)
        st.write(f"<h4>Nível de defesa: {data['stats'][2]['base_stat']}</h4>", unsafe_allow_html=True)


# Define o layout da aplicação
def app():
    st.markdown("<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>BUSQUE O SEU POKEMON!</h1>", unsafe_allow_html=True)
    st.markdown("Digite o nome ou número do Pokémon que você quer buscar:")
    pokemon_name = st.text_input("Nome ou número")
    if st.button("Buscar"):
        if pokemon_name.strip() == "":
            st.error("Digite o nome ou número do Pokémon")
        else:
            show_pokemon_info(pokemon_name.lower())


# Executa
if __name__ == "__main__":
    app()

