# import os
from nbformat import write
import streamlit as st
from reference import constants, map
# import matplotlib as mpl
# import graphviz

import generate_map as rmap

st.title('Review Randomization')

# Iniitialize state
if 'seed' not in st.session_state:
    st.session_state['seed'] = ''
if 'starting_weapon' not in st.session_state:
    st.session_state['starting_weapon'] = 'SWORD_OF_LIFE'
if 'magician_item' not in st.session_state:
    st.session_state['magician_item'] = 'RANDOM'
if 'world_type' not in st.session_state:
    st.session_state['world_type'] = 'VANILLA'
if 'debug' not in st.session_state:
    st.session_state['debug'] = False

ready = False

with st.sidebar:
    #     arguments = {
    #     'seed': None,
    #     'starting_weapon': 'SWORD_OF_LIFE',
    #     'magician_item': 'RANDOM',
    #     'world_type': 'vanilla',
    #     'trash': 'vanilla',
    #     'plan': [],
    #     'randbomize_hubs': False, # Not an implemented feature yet...
    #     'debug': False,
    # }
    st.session_state['seed'] = st.text_input('Seed', st.session_state['seed'])

    sword_list = map.SWORDS
    if 'RANDOM' not in sword_list:
        sword_list.append('RANDOM')
    st.session_state['starting_weapon'] = st.radio('Starting Weapon', sword_list)

    st.session_state['magician_item'] = st.text_input('Magician Item', 'RANDOM').upper()

    st.session_state['world_type'] = st.radio('World Type', constants.VALID_WORLD_TYPES)

    if st.button('Toggle DEBUG'):
        if st.session_state['debug']:
            st.session_state['debug'] = False 
        else:
            st.session_state['debug'] = True

    if st.button('Reset Session'):
        for key in st.session_state:
            del st.session_state[key]

# input_settings = 
st.write('seed', st.session_state['seed'])
st.write('starting_weapon', st.session_state['starting_weapon'])
st.write('magician_item', st.session_state['magician_item'])
st.write('world_type', st.session_state['world_type'])
st.write('debug', st.session_state['debug'])

if st.button('BLAZE IT!'):
    ready = True

if ready:
    world_graph = rmap.initialize_world({
    'seed': st.session_state['seed'],
    'starting_weapon': st.session_state['starting_weapon'],
    'magician_item': st.session_state['magician_item'],
    'world_type': st.session_state['world_type'],
    'debug': st.session_state['debug'],
})
    randomization = rmap.randomize_items(world_graph, {
    'seed': st.session_state['seed'],
    'starting_weapon': st.session_state['starting_weapon'],
    'magician_item': st.session_state['magician_item'],
    'world_type': st.session_state['world_type'],
    'debug': st.session_state['debug'],
})

    # st.json(randomization, expanded=False)
    for act in randomization.keys():
        with st.expander('Act ' + str(act), expanded=False):
            for item in randomization[act]:
                # write_string = item['placement']['type'] + ' ' + item['placement']['name'] + ' \n'
                # write_string += '@ \n'
                # write_string += item['location']['type'] + ' ' + item['location']['name']
                # st.write(item['placement']['type'] + ' ' + item['placement']['name'])
                # st.write('@')
                # st.write(item['location']['type'] + ' ' + item['location']['name'])
                st.write(item)
