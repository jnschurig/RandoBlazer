import streamlit as st 
import generate_map as map_gen, random_manager as rm
from reference import map, constants, rom_data, web_constants
import json

def go():
    # Base dictionary
    settings_dict = {
        'seed': None,
        'starting_weapon': 'SWORD_OF_LIFE',
        'magician_item': 'RANDOM',
        'world_type': 'vanilla',
        'trash_mode': 'vanilla',
        'trash': [],
        'plan': [],
        'only_required': False, 
        'randomize_hubs': False, # Not an implemented feature yet...
        'gem_scaling': 1, 
        'debug': False,
        'verbose': False,
    }

    if 'completed' not in st.session_state:
        st.session_state['completed'] = {}
    if 'settings' not in st.session_state:
        st.session_state['settings'] = settings_dict

    st.markdown('### Randomizer Options')
    main_col1, main_col2 = st.columns([3, 1])
    # default_seed = rm.number_list_to_str(rm.number_to_base(rm.get_random_int(0, 99999999999999), 36))
    with main_col1:
        with st.form(key='rando_submit_form'):
            form_col_1, form_col_2 = st.columns(2)

            with form_col_1:
                settings_dict['seed'] = st.text_input('Seed', value='0')
                settings_dict['starting_weapon'] = st.selectbox('Starting Sword', ['RANDOM'] + map.SWORDS, index=1, help=map_gen.starting_weapon_help)
                magician_item_list = ['RANDOM']
                magician_item_list += list(rom_data.ITEMS.keys())
                settings_dict['magician_item'] = st.selectbox('Magician Item', magician_item_list, index=0, help=map_gen.magician_item_help)
                settings_dict['world_type'] = st.selectbox('World Graph Generation', constants.VALID_WORLD_TYPES, index=2, help=map_gen.world_type_help)
                # settings_dict['plan'] = ''
                settings_dict['gem_scaling'] = st.slider('Gem Scaling', 0, 10, 1, 1, help='Gem scale multiplier. 1 = vanilla gem amounts.')

            with form_col_2:
                settings_dict['trash_mode'] = st.selectbox('Trash Fill Method', constants.TRASH_FILL_METHODS, index=0)
                # settings_dict['trash'] = st.selectbox('Trash Fill Items', constants.VALID_TRASH_SETTINGS, index=0)
                trash_list = st.multiselect('Trash Item Selection', list(rom_data.ITEMS.keys()), help='Only works when "<ITEM>" is selected. ')

                settings_dict['only_required'] = st.selectbox('Only Required', [False, True], help='Not yet implemented. Replaces all non-required items (such as bracelets) with trash item(s)')
                # settings_dict['randomize_hubs'] = st.selectbox('Randomize Hubs', [False, True], help='Not implemented. Option does nothing.')

            submitted = st.form_submit_button('Blaze it!')
            # submitted = st.button('Blaze it!')

            if submitted:
                if 'completed' in st.session_state:
                    # Clear out a previous run generation...
                    st.session_state['completed'] = {}
                # if settings_dict['trash'] == ['<ITEM>']:
                #     settings_dict['trash'] = trash_list
                if not settings_dict['seed'] or settings_dict['seed'] == '0':
                    settings_dict['seed'] = None
                settings_dict['seed'] = rm.start_randomization(settings_dict['seed'])
                world_graph = map_gen.initialize_world(settings_dict)
                with st.spinner('Generating World Graph'):
                    st.session_state['completed'] = map_gen.randomize_items(world_graph, settings_dict)
                with st.spinner('Randomizing Items and Lairs'):
                    st.session_state['settings'] = settings_dict
                # submitted = False
                # st.session_state.submitted = False
    
        button_space, right_space = st.columns([1, 2])

    with main_col2:
        st.markdown('#### Settings Dictionary')
        st.json(settings_dict)


    st.markdown('---')

    if st.session_state['completed'] != {}:
        with right_space:
            st.markdown('##### Seed: `' + st.session_state['completed']['settings']['seed'] + '`')

        with button_space:
            st.download_button(
                'Download JSON',
                data=json.dumps(st.session_state['completed'], indent=4),
                file_name='rando_logic_' + str(settings_dict['seed']) + '.json',
                use_container_width=True,
            )
        for key in st.session_state['completed'].keys():
            if key != 'settings':
                if len(str(key)) == 1:
                    label = 'Sphere ' + str(key)
                else:
                    label = str(key)
                with st.expander(label):
                    # st.json(st.session_state['completed'][key])

                    header_col1, header_col2 = st.columns([1, 1], gap='medium')

                    with header_col1:
                        st.markdown('### Location')

                    with header_col2:
                        st.markdown('### Check')

                    for check in st.session_state['completed'][key]:
                        sphere_col1, sphere_col2 = st.columns([1, 1], gap='medium')
                        with sphere_col1:
                            st.json(check['location'])

                        with sphere_col2:
                            st.json(check['placement'])
                        st.markdown('---')
            # else:
            #     label = str(key)
        # st.write(st.session_state['completed'].keys())



    return 

if __name__ == '__main__':
    use_title = 'RandoBlazer Generator Sim'
    st.set_page_config(
        page_title=use_title,
        page_icon='🗡️',
        layout='wide',
        initial_sidebar_state='auto',
        menu_items={
            'About': '''
            For questions or issues, feel free to contact jnschurig@gmail.com 
            
            See the [Github Repository](https://github.com/jnschurig/RandoBlazer)
            '''
        }
    )
    with st.sidebar:
        st.image('snes_soulblazer_logo.webp')
        st.markdown(web_constants.SIDEBAR_TEXT)
    # st.markdown('### ' + use_title)
    go()
