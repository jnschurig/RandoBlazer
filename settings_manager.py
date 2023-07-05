import sys, getopt
import json
import streamlit as st
import networkx as nx

from reference import map, constants, rom_data
import random_manager as rm
import build_world as bw

valid_args = '''Valid Arguments:
-h                --help                       | Information about the script. 
-s <Seed>         --seed        <Seed>         | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-a                --race_mode                  | Don't output a spoiler log because it is race mode.
-d                --debug                      | Enable detailed output for debugging. Default is False. 
'''

help_info = '''Help Info: 
This script will modify the contents ROM data and replace bits of it with other data. 
The arguments are intended to be used for testing by running this script all by itself. 
'''

def main(argv):
    arguments = {
        'seed': None,
        'race_mode': False,
        'debug': False,
        'verbose': False,
        'cli_execution': False
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:adv',['help','seed=','race_mode','debug','verbose',])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            arguments['cli_execution'] = True
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-s', '--seed'):
            arguments['cli_execution'] = True
            arguments['seed'] = arg
        elif opt in ('-a', '--race_mode'):
            arguments['cli_execution'] = True
            arguments['race_mode'] = True
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
        elif opt in ('-v', '--verbose'):
            arguments['debug'] = True
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments

# dict output format...
# For progressive items, order is NOT important. 
# We will use this list to confirm the existence of 
# items in the map document. 
# ''' 
# sword_use_list = []
# for sword in map.SWORDS:
#     if sword in settings['swords]['entries']:
#         sword_use_list.append(sword)
# # This will return a correctly ordered list of swords.
# '''

# Functional logic for updating the "optional_logic" key
for key in map.ADDITIONAL_LOGIC_REQUIREMENTS.keys():
    for key_region in map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['regions']:
        map.REGIONS[key_region]['requirements'] += map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['requirements']

def display_progressive_option(name, progressive_option=None):

    name_title = name.replace('_', ' ').title()

    with st.expander(name_title + ' Availability Options'):

        settings = {
            'progressive': False,
            'entries': []
        }

        if progressive_option is not None:
            # progressive = st.radio(
            progressive = st.checkbox(
                'Progressive ' + name_title, 
                value=progressive_option,
                # (False, True), 
                # horizontal=True, 
                # index=progressive_option, 
                key='progressive_' + name
            
            )
            settings['progressive'] = progressive

        availability_selection = st.radio(
            name_title + ' Availability', 
            ['All', 'Partial'], 
            horizontal=True, 
            key=name + '_partial_selection'
        )

        if availability_selection == 'Partial':
            selected_items = st.multiselect(
                'Available ' + name_title, 
                map.OPTIONS_LOOKUP[name], 
                key=name + '_choices'
            )

            temp_list = []
            for item in map.OPTIONS_LOOKUP[name]:
                if item in selected_items:
                    temp_list.append(item)

            settings['entries'] = temp_list
        
        else:
            settings['entries'] = map.OPTIONS_LOOKUP[name]

    return settings

def display_optional_logic_options():
    optional_logic = {}

    for key in map.ADDITIONAL_LOGIC_REQUIREMENTS.keys():
        is_enabled = st.checkbox(
            map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['name'], 
            value=False,
            help=map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['description'],
            key='optional_logic_' + key.lower(),
            )
        
        if is_enabled:
            for region in map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['regions']:
                optional_logic[region] = map.ADDITIONAL_LOGIC_REQUIREMENTS[key]['requirements']
    return optional_logic

# def session_list_pop(session_key_name, list_idx=0):
#     return
#     # return st.session_state[session_key_name].pop(list_idx)
    
def reset_session_var(session_key_name):
    if session_key_name in st.session_state:
        del st.session_state[session_key_name]
    return 

def get_last_trash_idx():
    if 'trash_dict' not in st.session_state or st.session_state['trash_dict'] == {}:
        return None
    
    current_key = 0 
    for key in st.session_state['trash_dict'].keys():
        if key > current_key:
            current_key = key

    return current_key

def rekey_dict(input_dict=None):
    if input_dict is None:
        return {}

    new_dict = {}
    index = 0
    
    for key in input_dict.keys():
        new_dict[index] = input_dict[key]
        index += 1

    return new_dict

def display_trash_options():
    # base_trash_dict = {}
    # for idx, key in enumerate(list(constants.VANILLA_TRASH_WEIGHTS.keys())):
    #     base_trash_dict[idx] = (key, constants.VANILLA_TRASH_WEIGHTS[key])

    if 'trash_dict' not in st.session_state or st.session_state['trash_dict'] == {}:
        st.session_state['trash_dict'] = {}
        for idx, key in enumerate(list(constants.VANILLA_TRASH_WEIGHTS.keys())):
            st.session_state['trash_dict'][idx] = (key, constants.VANILLA_TRASH_WEIGHTS[key])

    all_items = rom_data.all_items_list(pretty_names=True)



    # if 'trash_count' not in st.session_state:
    #     st.session_state['trash_count'] = len(constants.VANILLA_TRASH_WEIGHTS.keys())

    # use_custom_trash = st.checkbox('Customize Trash Settings', value=False, key='use_custom_trash_box')

    widget_enabled_setting = not st.checkbox('Customize Trash Settings', value=False, key='use_custom_trash_box')

    trash_top_row_left, trash_top_row_right = st.columns(2)

    with trash_top_row_left:
        last_trash = get_last_trash_idx()
        new_key = 0
        if last_trash is None:
            new_key = 0
        else:
            new_key = last_trash + 1

        if st.button('Add Trash Item', disabled=widget_enabled_setting):
            st.session_state['trash_dict'][new_key] = ('NOTHING', 1)

    with trash_top_row_right:
        if st.button('Reset Trash Settings', disabled=widget_enabled_setting):
            if 'trash_dict' in st.session_state:
                st.session_state['trash_dict'] = {}
                st.experimental_rerun()

    trash_display_iterator = []
    for key in st.session_state['trash_dict'].keys():
        # trash_display_iterator.append((st.session_state['trash_dict'][key], key))
        triple_tuple = (st.session_state['trash_dict'][key][0], st.session_state['trash_dict'][key][1], key)
        trash_display_iterator.append(triple_tuple)

    for key, item_tuple in enumerate(trash_display_iterator):
        tcol1, tcol2, tcol3 = st.columns([2, 2, 1])

        item = item_tuple[0]
        weight = item_tuple[1]
        dict_key = item_tuple[2]

        pretty_item = rom_data.ITEMS[item]['pretty_name']
        pretty_item_idx = all_items.index(pretty_item)
        with tcol1:
            # st.write(item)
            chosen_item = st.selectbox(
                pretty_item, 
                all_items,
                index=pretty_item_idx,
                label_visibility='collapsed',
                key='trash_item_' + str(key),
                # on_change=session_list_pop('trash_list', key),
                disabled=widget_enabled_setting,
            )

            use_item = rom_data.pretty_name_lookup_dict()[chosen_item]


        with tcol2:
            # st.write(weight)
            item_weight = st.number_input(
                pretty_item,
                constants.WEIGHTS_ABSOLUTE_MIN_MAX[0],
                constants.WEIGHTS_ABSOLUTE_MIN_MAX[1],
                value=weight,
                label_visibility='collapsed',
                key='trash_weight_' + str(key),
                disabled=widget_enabled_setting,
            )

        st.session_state['trash_dict'][key] = (use_item, item_weight)

        with tcol3:
            # st.write('button')
            if st.button('Remove', key='remove_trash_button_' + str(key), disabled=widget_enabled_setting):
                del st.session_state['trash_dict'][dict_key]
                st.session_state['trash_dict'] = rekey_dict(st.session_state['trash_dict'])
                st.experimental_rerun()

    # st.json(st.session_state['trash_dict'])
    formatted_trash_dict = {}
    for key in st.session_state['trash_dict'].keys():
        formatted_trash_dict[st.session_state['trash_dict'][key][0]] = st.session_state['trash_dict'][key][1]
    return formatted_trash_dict

def display_options(settings_dict):
    if settings_dict['seed'] is None:
        settings_dict['seed'] = ''
    seed_value = st.text_input('Seed', key='input_seed', placeholder='Random Seed', label_visibility='collapsed')
    settings_dict['seed'] = rm.start_randomization(seed_value)


    st.markdown('#### Item Availability')
    formatted_settings = {
        'seed': settings_dict['seed'],
        'swords': {},
        'armor': {},
        'bracelets': {},
        'stones': {},
        'red_hots': {},
        'optional_logic': {},
        'trash': {},
    }

    with st.container():
        formatted_settings['swords'] = display_progressive_option('swords', None)
        formatted_settings['armor'] = display_progressive_option('armor', None)
        formatted_settings['bracelets'] = display_progressive_option('bracelets', True)
        formatted_settings['stones'] = display_progressive_option('stones', True)
        formatted_settings['red_hots'] = display_progressive_option('red_hots', True)
    
    with st.container():
        st.markdown('#### Optional Logic')

        formatted_settings['optional_logic'] = display_optional_logic_options()

    with st.container():
        st.markdown('#### Trash')

        formatted_settings['trash'] = display_trash_options()

    with st.sidebar:
        st.markdown('#### Session State')
        st.json(st.session_state)
    
    return formatted_settings

def compile_settings_string(settings_dict, settings_string=''):

    formatted_settings={}

    return formatted_settings

# def rando(seed: str=None):
#     settings_dict = {'seed': None}
#     # st.set_page_config(
#     #     page_title='Regional Progression Graph',
#     #     layout='wide'
#     # )
#     seed_value = st.text_input('Seed', value='', key='input_seed')
#     if seed_value:
#         settings_dict['seed'] = seed_value
#     settings_dict['world_type'] = st.selectbox('Network Generation Method', constants.VALID_WORLD_TYPES)
#     if st.button('Draw it...'):
#         world_graph = nx.DiGraph(bw.initialize_world(settings_dict))

#     return world_graph

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    if settings_dict['cli_execution']:
        detailed_settings = compile_settings_string(settings_dict)
        print(json.dumps(detailed_settings, indent=4))

    else:
        detailed_settings = display_options(settings_dict)
        st.markdown('#### Settings Dictionary')
        st.json(detailed_settings)
    # if settings_dict['debug']:
    #     print(json.dumps(settings_dict, indent = 4))

    # rando_result = randomizer(settings_dict)
    # print(rando_result)
