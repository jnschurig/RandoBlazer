import streamlit as st
from reference import constants, map

import build_world as bw
import random_manager as rm
import networkx as nx
# import matplotlib.pyplot as plt
import plotly.graph_objects as pgo

node_color_lookup = {
    1: '#1f77b4',  # muted blue
    2: '#ff7f0e',  # safety orange
    3: '#2ca02c',  # cooked asparagus green
    4: '#d62728',  # brick red
    5: '#9467bd',  # muted purple
    6: '#8c564b',  # chestnut brown
    7: '#e377c2',  # raspberry yogurt pink
    8: '#7f7f7f',  # middle gray
    9: '#bcbd22',  # curry yellow-green
    10: '#17becf'   # blue-teal
}

# def set_node_coordinates(digraph_obj, root_node=0, edge_x=None, edge_y=None, node_x=None, node_y=None, iteration=0):
def D_set_node_coordinates(digraph_obj, root_node=0, position_dict=None, iteration=0, x_dist=5, y_dist=5):
    # initialize

    if position_dict is None: position_dict = {
            'nodes': {root_node: {'x': 1 * x_dist, 'y': iteration * y_dist}},
            'edges': {},
            }

    # if root_node not in position_dict:
    #     position_dict['nodes'][root_node] = {'x': 1 * x_dist, 'y': iteration * y_dist}

    next_iteration = iteration + 1
    child_number = 0
    for child in digraph_obj.neighbors(root_node):
        child_number += 1
        position_dict['nodes'][child] = {'x': (child_number + iteration) * x_dist, 'y': next_iteration * y_dist}
        # position_dict['nodes'][child] = {'x': (child_number * x_dist), 'y': next_iteration * y_dist}
        position_dict = set_node_coordinates(digraph_obj, child, position_dict, next_iteration, x_dist, y_dist)

    return position_dict

def set_node_coordinates(digraph_obj, node=0, position_dict=None, iteration=0, x_dist=5, y_dist=10, vertical_spacing=10, child_idx=0, child_count=0):
    # initialize

    if position_dict is None: position_dict = {
            'nodes': {},
            'edges': {},
            }
        
    node_info = map.REGIONS[node]
    if 'is_act_hub' in node_info and node_info['is_act_hub']:
        iteration = 0
        new_y_dist = node_info['act'] * vertical_spacing * -1
        position_dict['nodes'][node] = {
            'x': 0,
            'y': new_y_dist,
        }
    else:
        new_y_dist = y_dist
        position_dict['nodes'][node] = {
            # 'x': (iteration * x_dist) + 1,
            'x': (iteration) * x_dist - (x_dist * child_idx / child_count),
            # 'y': (node_info['act'] + child_idx) * y_dist,
            # 'y': (node_info['act'] * y_dist) + child_idx,
            'y': y_dist,
        }

    child_count = 0
    for child in digraph_obj.neighbors(node):
        child_count += 1
        
    iteration += 1
    # child_count = len(digraph_obj.neighbors(node))
    for idx, child in enumerate(digraph_obj.neighbors(node)):
        child_v_spacing = (vertical_spacing * .9)
        child_y_dist = new_y_dist - (child_v_spacing * idx / child_count)
        position_dict = set_node_coordinates(digraph_obj, child, position_dict, iteration, x_dist, child_y_dist, child_idx=idx, child_count=child_count)

    return position_dict

def draw_plotly_graph(digraph_obj, position_dict, chart_height=1200, apply_colors=True):
    edge_x = []
    edge_y = []
    for edge in digraph_obj.edges():
        # x0, y0 = digraph_obj.nodes[edge[0]]['pos']
        # x1, y1 = digraph_obj.nodes[edge[1]]['pos']
        edge_name = str(edge[0]) + '-' + str(edge[1])
        x0 = position_dict['edges'][edge_name]['x0']
        x1 = position_dict['edges'][edge_name]['x1']
        y0 = position_dict['edges'][edge_name]['y0']
        y1 = position_dict['edges'][edge_name]['y1']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = pgo.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_color = []
    node_text = []
    for node in digraph_obj.nodes():
        # x, y = digraph_obj.nodes[node]['pos']
        x = position_dict['nodes'][node]['x']
        y = position_dict['nodes'][node]['y']
        node_x.append(x)
        node_y.append(y)
        node_color.append(node_color_lookup[map.REGIONS[node]['act']])
        # node_text.append(str(node))

        node_text.append(map.REGIONS[node]['detail'])

    if not apply_colors: node_color=[]

    node_trace = pgo.Scatter(
        x=node_x,
        y=node_y,
        mode='markers',
        hoverinfo='text',
        text=node_text,
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            # color=[],
            color=node_color,
            size=15, # Node Size
            # colorbar=dict(
            #     thickness=15,
            #     title='Node Connections',
            #     xanchor='left',
            #     titleside='right'
            # ),
            line_width=2,
        ),
    )
    
    fig = pgo.Figure(data=[edge_trace, node_trace],
        layout=pgo.Layout(
            title='<br>Logical Progression by Region',
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            annotations=[ dict(
                # text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                text="World Gen",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002 ) ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            # autosize=True
            height=chart_height
        )
    )
    
    return fig

def go(settings_dict={'seed': None, 'world_type': 'vanilla'}, nx_graph=None):
    if nx_graph is None:
        st.write('No graph detected')
        return None
    
    left_col, right_col = st.columns([1, 4])

    position_dict = set_node_coordinates(nx_graph, 37, x_dist=1, y_dist=1)

    for edge in nx_graph.edges():
        # st.write(type(edge))
        # st.write(edge)

        edge_name = str(edge[0]) + '-' + str(edge[1])

        position_dict['edges'][edge_name] = {
            'x0': position_dict['nodes'][edge[0]]['x'],
            'x1': position_dict['nodes'][edge[1]]['x'],
            'y0': position_dict['nodes'][edge[0]]['y'],
            'y1': position_dict['nodes'][edge[1]]['y'],
        }
    # set_node_coordinates(nx_graph.reverse())

    with left_col:
        st.write('Settings')
        st.write(settings_dict)

        # st.write(nx_graph.nodes())

        # st.write(nx_graph.edges())

        st.write('Node Positions')
        st.json(position_dict, expanded=False)

    with right_col:
        plotly_fig = draw_plotly_graph(nx_graph, position_dict)

        
        st.plotly_chart(plotly_fig, use_container_width=True)

    return 

if __name__ == '__main__':
    settings_dict = {'seed': None}
    st.set_page_config(
        page_title='Regional Progression Graph',
        layout='wide'
    )
    seed_value = st.text_input('Seed', value='', key='input_seed')
    if seed_value:
        settings_dict['seed'] = seed_value
    settings_dict['world_type'] = st.selectbox('Network Generation Method', constants.VALID_WORLD_TYPES)
    if st.button('Draw it...'):
        settings_dict['seed'] = rm.start_randomization(settings_dict['seed'])
        world_graph = bw.initialize_world(settings_dict)
        go(settings_dict, world_graph)