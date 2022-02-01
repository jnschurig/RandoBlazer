import os
import networkx as nx
from reference import map
import random_manager

def randomize_map():
    region_map = map.REGIONS
    region_id_list = list(region_map.keys())
    act_hubs = []

    # Identify region hubs
    print(region_id_list)
    for region_id in region_id_list:
        if 'is_act_hub' in region_map[region_id] and region_map[region_id]['is_act_hub']:
            act_hub = {
                'act': region_map[region_id]['act'],
                'hub_region': region_id
            }
            act_hubs.append(act_hub)
    
    # Map regions relative to the hub
    for act in act_hubs:
        act['sub_regions'] = []
        # Go through the regions AGAIN
        for region_id in region_id_list:
            if region_map[region_id]['act'] == act['act']:
                if act['hub_region'] != region_id:
                    act['sub_regions'].append(region_id)

    print(act_hubs)

    world_graph = nx.DiGraph()

    # Connect hubs...
    previous_node = None 
    used_regions = []

    for hub in act_hubs:
        if previous_node is not None:
            world_graph.add_edge(hub['hub_region'], previous_node['hub_region'])
            pass
        previous_node = hub
        used_regions.append(hub['hub_region'])

    # Randomly connect all other regions...
    for region in region_id_list:
        if region not in used_regions:
            # It's safe to add this region to the network.
            source_node = random_manager.get_random_list_member(used_regions)
            world_graph.add_edge(source_node, region)
            used_regions.append(region)

    print(world_graph)

    all_neighbors = get_all_neighbors(world_graph, 0)
    print(all_neighbors)
    print(list(world_graph.neighbors(0)))

# 1. Go to first hub area.
# 2. Get list of all "connected" regions in the graph to that hub area.
# 3. Get list of requirements for NEXT hub area. 
# 4. Place required checks randomly in any compatible areas in regions from #2.
# 4. ALT - Get a list of all requirements for next hub area and connected regions (in or below the same hub) and fulfill those requirements randomly.
# 5. Move to the next hub and combine all related regions in the same hub OR below. Get a list of requirements and fulfill them randomly.
# 6. Repeat. Keep a list of fulfilled requirements so we can know which items can go in which places.

    return True

def get_all_neighbors(graph, node):
    neighbor_list = []
    for neighbor in graph.neighbors(node):
        neighbor_list.append(neighbor)
        neighbor_list += get_all_neighbors(graph, neighbor)

    unique_list = []
    for member in neighbor_list:
        if member not in unique_list:
            unique_list.append(member)
    return unique_list


if __name__ == '__main__':
    # Run this with creds built in.
    random_manager.start_randomization('hi')
    randomize_result = randomize_map()
    print(randomize_result)