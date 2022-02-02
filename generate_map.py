# import os
import random
import sys
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

    # Add 'next hub region' to act hubs.
    # Not super proud of this, but it does work.
    idx = 0
    for hub in act_hubs:
        idx += 1
        if hub['act'] != 7:
            hub['next_hub_region'] = act_hubs[idx]['hub_region']
        # else: # I don't think we need a self reference here.
        #     hub['next_hub_region'] = hub['hub_region']
    
    # Map regions relative to the hub
    for act in act_hubs:
        act['sub_regions'] = []
        # Go through the regions AGAIN
        for region_id in region_id_list:
            if region_map[region_id]['act'] == act['act']:
                if act['hub_region'] != region_id:
                    act['sub_regions'].append(region_id)

    print(act_hubs)

    # Build a randomized directional graph for determining eligible areas 
    # for requirement fulfillment (placing checks)
    world_graph = nx.DiGraph()

    # Connect hubs...
    previous_node = None 
    used_regions = []

    # Hubs need to be chronilogical, not random.
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

    # print(world_graph)

    # all_neighbors = get_all_neighbors(world_graph, 6)
    # print(all_neighbors)
    # print(list(world_graph.neighbors(0)))

    # Discover the "next" hub region and record it in the current act.
    # 0. Initialize fulilled requirements and placed items...
    all_reqs = []
    fulfilled_reqs = []
    placed_checks = []
    valid_regions = []
    # 1. Go to first hub area.
    for hub in act_hubs:
        # Determine valid regions
        valid_regions.append(hub['hub_region'])
        # 2. Get list of all "connected" regions in the graph to that hub area.
        current_neighbors = get_all_neighbors(world_graph, hub['hub_region'])
        if hub['hub_region'] not in current_neighbors:
            current_neighbors.append(hub['hub_region'])
        next_hub_reqs = []
        if 'next_hub_region' in hub:
            # 3. Get the 'next' hub region.
            if hub['next_hub_region'] not in valid_regions:
                valid_regions.append(hub['next_hub_region'])
            current_neighbors.append(hub['next_hub_region'])
            next_hub_reqs = region_map[hub['next_hub_region']]['requirements']

        valid_regions += hub['sub_regions']
        # Trim current_neighbors down to only valid regions.
        valid_neighbors = []
        for neighbor in current_neighbors:
            if neighbor in valid_regions:
                valid_neighbors.append(neighbor)

        # 4. Combine all known requirements for "accessible" areas.
        local_reqs = []
        for local_region in valid_neighbors:
            local_reqs += region_map[local_region]['requirements']
        
        local_reqs = distinctify(local_reqs)
        all_reqs += local_reqs
        # 5. Pick a requirement at random and fulfill it in a random region which does NOT require it.
        next_hub_not_available = True
        while next_hub_not_available:
            # Fulfill at least one requirement from the list.
            current_req = random_manager.get_random_list_member(local_reqs)
            print(current_req)
            print(valid_neighbors)
            # sys.exit('temp breaking point')
            req_not_fulfilled = True
            while req_not_fulfilled:
                # Pick a random region in the valid_neighboars
                target_region = random_manager.get_random_list_member(valid_neighbors)
                if current_req not in region_map[target_region]['requirements']:
                    # Place the item!
                    if current_req['type'] == 'npc_id':
                        # pick a lair location from checks.
                        pass 
                    if current_req['type'] == 'item':
                        # Check to see if item already obtained.
                        # If not, pick a chest or item location from checks.
                        # Add item to items allocated list.
                        pass 
                    if current_req['type'] == 'flag':
                        # Check to see if flag already fulfilled
                        # Pick a random item from one of the FLAGS
                        # Put it in a random item or chest location from checks.
                        # Add item to items obtained list.
                        pass
                    else:
                        # No place to put it. Do another loop
                        pass
                    placed_checks.append('placeholder')
                    fulfilled_reqs.append(current_req)
                    # This ^ should be a json object which shows a 'requirement' being in a 'check'
                    req_not_fulfilled = False
                # Temp line to break the loop.
                

            # Check to see if the next hub is available based on fulfilled requirements.
            if all(elem in fulfilled_reqs for elem in next_hub_reqs):
                next_hub_not_available = False

        print(local_reqs)
    # 6. Check to see if latest 'hub' requirement is met. If so, add new regions and recompile requirements.

    return True

# Input a list which may or may not be unique.
# Output a list which is definitely unique.
# If input is not a list type, return the same thing without changes.
def distinctify(non_unique_list):
    if type(non_unique_list) is not list:
        return non_unique_list
    else:
        unique_list = []
        for item in non_unique_list:
            if item not in unique_list:
                unique_list.append(item)
    return unique_list

def get_all_neighbors(graph, node):
    neighbor_list = []
    for neighbor in graph.neighbors(node):
        neighbor_list.append(neighbor)
        neighbor_list += get_all_neighbors(graph, neighbor)

    # unique_list = []
    # for member in neighbor_list:
    #     if member not in unique_list:
    #         unique_list.append(member)
    # return unique_list
    return distinctify(neighbor_list)


if __name__ == '__main__':
    # Run this with creds built in.
    random_manager.start_randomization('hi')
    randomize_result = randomize_map()
    print(randomize_result)