#!/usr/local/bin/python3

###################################################################################################
#                                                                                                 #
# SCRIPT FILE: main.py                                                                            #
# CREATION DATE: 02/02/2023                                                                       #
# HOUR: 10:10                                                                                     #
# DISTRIBUTION USED: UBUNTU                                                                       #
# OPERATIONAL SYSTEM: LINUX                                                                       #
#                                                                             DEVELOPED BY: BATES #
###################################################################################################
#                                                                                                 #
# SUMMARY: Start the project                                                                      #
#                                                                                                 #
###################################################################################################

import streamlit as st
from pokeapi import app as get_pokemon_data, show_pokemon_info
from forca import play_game
from PIL import Image
import json

with open('param/param.json') as f:
    keys = json.load(f)

image = keys['icon']
logo = keys['logo']
img = Image.open(image)
icon = img.resize((50, 50))


# Define a função para a página inicial
def home():
    st.image(logo)
    st.write("Bem-vindo(a) ao site completo do Pokémon.")
    st.write("Aqui você pode jogar e também pesquisar Pokémons!")


# Define o menu de navegação

# Executa a aplicação
def run():
    st.set_page_config(page_title="Pokemon", page_icon=icon, layout="wide", initial_sidebar_state="collapsed")
    st.markdown("<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>", unsafe_allow_html=True)
    menu = {
    "Home": home,
    "Adivinha": play_game,
    "Buscar Pokémon": get_pokemon_data
    }

    # Exibe o menu de navegação
    menu_choice = st.sidebar.radio("Selecione uma opção", list(menu.keys()))
    menu[menu_choice]()

if __name__ == "__main__":
    run()
