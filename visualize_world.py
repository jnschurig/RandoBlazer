# import os
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
# import matplotlib as mpl
# import graphviz

import generate_map_v2 as rmap

vis_map = rmap.randomize_map()

st.write('Map Viewer')

nx.draw_networkx(vis_map)
plt.show()

# G = nx.petersen_graph()

# subax1 = plt.subplot(121)

# nx.draw(vis_map, with_labels=True, font_weight='bold')

# subax2 = plt.subplot(122)

# nx.draw_shell(vis_map, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

# plt.show()

# # BEGIN pyplot example
# pos = nx.layout.spring_layout(vis_map)

# node_sizes = [3 + 10 * i for i in range(len(vis_map))]

# # st.write(vis_map.number_of_edges())
# edge_count = vis_map.number_of_edges()
# edge_colors = range(2, edge_count + 2)
# edge_alphas = [(5 + i) / (edge_count + 4) for i in range(edge_count)]

# nodes = nx.draw_networkx_nodes(vis_map, pos, node_size=node_sizes, node_color='blue')
# edges = nx.draw_networkx_edges(vis_map, pos, node_size=node_sizes, arrowstyle='->',
#                                arrowsize=10, edge_color=edge_colors,
#                                edge_cmap=plt.cm.Blues, width=2)

# for i in range(edge_count):
#     edges[i].set_alpha(edge_alphas[i])

# pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
# pc.set_array(edge_colors)
# plt.colorbar(pc)

# ax = plt.gca()
# ax.set_axis_off()
# plt.show()
# # END pyplot example

# st.pyplot()

# st.graphviz_chart(vis_map)

# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt

# st.title('Hello Networkx')
# st.markdown('Zachary´s Karate Club Graph')


# G = nx.karate_club_graph()


# fig, ax = plt.subplots()
# pos = nx.kamada_kawai_layout(G)
# nx.draw(G,pos, with_labels=True)
# st.pyplot(fig)
# st.balloons()

# fig, ax = plt.subplots() 
# pos = nx.kamada_kawai_layout(vis_map)
# nx.draw(vis_map, pos, with_labels=True)

# st.pyplot(fig)
# st.balloons()