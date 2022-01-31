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
        act['region_list'] = []
        # Go through the regions AGAIN
        for region_id in region_id_list:
            if region_map[region_id]['act'] == act['act']:
                act['region_list'].append(region_id)

    print(act_hubs)
    # print(map.REGIONS[0])
    return True


if __name__ == '__main__':
    # Run this with creds built in.
    randomize_result = randomize_map()
    print(randomize_result)