# Using this https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/

import networkx as nx#, matplotlib as plt
import random 

# class graph_vis:
   
#     def __init__(self):
          
#         # visual is a list which stores all 
#         # the set of edges that constitutes a
#         # graph
#         self.visual = []
          
#     # addEdge function inputs the vertices of an
#     # edge and appends it to the visual list
#     def add_edge(self, a, b):
#         temp = [a, b]
#         self.visual.append(temp)
          
#     # In visualize function G is an object of
#     # class Graph given by networkx G.add_edges_from(visual)
#     # creates a graph with a given list
#     # nx.draw_networkx(G) - plots the graph
#     # plt.show() - displays the graph
#     def visualize(self):
#         G = nx.DiGraph()
#         G.add_edges_from(self.visual)
#         nx.draw_networkx(G)
#         plt.show()


g = nx.DiGraph()
# g = graph_vis()

all_nodes = list(range(79))
to_use_nodes = all_nodes
used_nodes = []

# There are 0-78 regions in SB
g.add_nodes_from(all_nodes)
# for x in range(79):
#     g.add_node(x)

used_nodes.append(to_use_nodes[0])
to_use_nodes.remove(0) # Don't want to have 0 join to itself.

for x in range(79-1):
    # if used_nodes == []:
    #     # We have a brand new network. Create it.
    #     first_node = to_use_nodes[random.randint(0, len(to_use_nodes) - 1)]
    # else:
        # We have an existing network. Add to it.
    source_node_idx = random.randint(0, len(used_nodes)-1)
    target_node_idx = random.randint(0, len(to_use_nodes)-1)
    target_node = to_use_nodes.pop(target_node_idx)

    g.add_edge(used_nodes[source_node_idx], target_node)
    used_nodes.append(target_node)
    print(str(used_nodes[source_node_idx]) + ',' + str(target_node))
    # to_use_nodes.pop(target_node_idx)

print(to_use_nodes)
print(len(to_use_nodes))
print(used_nodes)
print(len(used_nodes))
