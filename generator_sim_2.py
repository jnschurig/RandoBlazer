# Standard imports 
import streamlit as st
import networkx as nx

# Local imports
from reference import constants
import random_manager as rm
import build_world as bw
import draw_network
import place_items

def go(settings_dict={'seed': None}):
    world_graph = None
    if st.button('Draw it...'):
        settings_dict['seed'] = rm.start_randomization(settings_dict['seed'])
        world_graph = nx.DiGraph(bw.initialize_world(settings_dict))

    st.markdown('#### Seed: ' + str(settings_dict['seed']))

    if world_graph is not None:
        figure_placement_dict = draw_network.set_node_coordinates(world_graph, 37, x_dist=1, y_dist=1)
        figure_placement_dict = draw_network.set_edge_coordinates(world_graph, figure_placement_dict)
        plotly_fig = draw_network.draw_plotly_graph(world_graph, figure_placement_dict, chart_height=800)

        st.plotly_chart(plotly_fig, use_container_width=True)

    placement_result = place_items.go(world_graph)

    st.json(placement_result)

    return True 

if __name__ == '__main__':
    st.set_page_config(
        page_title='Logic Tester',
        layout='wide'
    )
    settings_dict = {'seed': None}
    seed_value = st.text_input('Seed', value='', key='input_seed')
    if seed_value:
        settings_dict['seed'] = seed_value
    settings_dict['world_type'] = st.selectbox('Network Generation Method', constants.VALID_WORLD_TYPES)
    go(settings_dict)
