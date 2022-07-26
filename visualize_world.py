import streamlit as st
from reference import constants, map

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
if 'trash_mode' not in st.session_state:
    st.session_state['trash_mode'] = 'VANILLA'
if 'trash' not in st.session_state:
    st.session_state['trash'] = []
if 'only_required' not in st.session_state:
    st.session_state['only_required'] = False
if 'gem_scaling' not in st.session_state:
    st.session_state['gem_scaling'] = 1
if 'debug' not in st.session_state:
    st.session_state['debug'] = False

ready = False

with st.sidebar:
    st.session_state['seed'] = st.text_input('Seed', st.session_state['seed'])

    sword_list = map.SWORDS
    if 'RANDOM' not in sword_list:
        sword_list.append('RANDOM')
    st.session_state['starting_weapon'] = st.radio('Starting Weapon', sword_list)

    st.session_state['magician_item'] = st.text_input('Magician Item', 'RANDOM').upper()

    st.session_state['world_type'] = st.radio('World Type', constants.VALID_WORLD_TYPES)

    st.session_state['trash_mode'] = st.radio('Trash Mode', constants.TRASH_FILL_METHODS)

    item_list = list(constants.VANILLA_TRASH_WEIGHTS.keys())
    item_list.sort()
    with st.expander('Trash Selection (Leave blank for vanilla)', expanded=False):
        for item in item_list:
            add_item = st.checkbox(item)
            if add_item and item not in st.session_state['trash']:
                st.session_state['trash'].append(item)
            elif not add_item and item in st.session_state['trash']:
                st.session_state['trash'].remove(item)

    st.session_state['only_required'] = st.radio('Only Required', [True, False], 1)

    st.session_state['gem_scaling'] = st.slider('Gem/Exp Scaling', 0.0, 10.0, 1.0, 0.1)

    if st.button('Toggle DEBUG'):
        if st.session_state['debug']:
            st.session_state['debug'] = False 
        else:
            st.session_state['debug'] = True

    if st.button('Reset Session'):
        for key in st.session_state:
            del st.session_state[key]

# input_settings = 
st.write('Seed:', st.session_state['seed'])
st.write('Starting Weapon:', st.session_state['starting_weapon'])
st.write('Magician Item:', st.session_state['magician_item'])
st.write('World Type:', st.session_state['world_type'])
st.write('Trash Mode:', st.session_state['trash_mode'])
st.write('Trash:', st.session_state['trash'])
st.write('Only Required:', st.session_state['only_required'])
st.write('Gem Scaling:', st.session_state['gem_scaling'])
st.write('debug:', st.session_state['debug'])

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
    'trash_mode': st.session_state['trash_mode'],
    'trash': st.session_state['trash'],
    'only_required': st.session_state['only_required'],
    'gem_scaling': st.session_state['gem_scaling'],
    'debug': st.session_state['debug'],
})

    # st.json(randomization, expanded=False)
    for act in randomization.keys():
        with st.expander(str(act), expanded=False):
            if type(randomization[act]) is dict:
                st.json(randomization[act])
            else:
                for item in randomization[act]:
                    st.write(item)
