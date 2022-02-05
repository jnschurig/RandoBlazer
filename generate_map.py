import os, json
# import random
import sys
import networkx as nx
from reference import map, constants, rom_data
import random_manager

def randomize_map():
    region_map = map.REGIONS
    region_id_list = list(region_map.keys())
    act_hubs = []

    # available_items = list(rom_data.ITEMS.keys())
    
    # 0. Initialize fulilled requirements and placed items...
    # all_reqs = []
    fulfilled_reqs = []
    placed_checks = []
    valid_regions = []
    placed_items = []
    spoiler_log = []

    # Identify region hubs
    # print(region_id_list)
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

    # print(act_hubs)

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
    # 1. Go to first hub area.
    for hub in act_hubs:
        # Determine valid regions
        # 2. Get list of all "connected" regions in the graph to that hub area.
        current_neighbors = get_all_neighbors(world_graph, hub['hub_region'])
        next_hub_reqs = []
        if 'next_hub_region' in hub:
            # 3. Get the 'next' hub region.
            # if hub['next_hub_region'] not in valid_regions:
            #     valid_regions.append(hub['next_hub_region'])
            # current_neighbors.append(hub['next_hub_region'])
            next_hub_reqs = region_map[hub['next_hub_region']]['requirements']

        valid_regions += hub['sub_regions']
        # Trim current_neighbors down to only valid regions.
        valid_neighbors = []
        for neighbor in current_neighbors:
            if neighbor in valid_regions:
                valid_neighbors.append(neighbor)

        # 4. Combine all known requirements for "accessible" areas.
        local_reqs = next_hub_reqs
        local_checks = []
        for local_region in valid_neighbors:
            # We can use requirements from next hub region, but not checks.
            local_reqs += region_map[local_region]['requirements']
            # if 'next_hub_region' in hub and local_region != hub['next_hub_region']:
            for local_check in region_map[local_region]['checks']:
                # all_check_reqs = []
                # for check_req in region_map[local_region]['requirements']:
                #     if
                local_check['check_requirements'] = region_map[local_region]['requirements']
                local_checks.append(local_check)
            # local_checks += region_map[local_region]['checks']
        valid_neighbors = random_manager.shuffle_list(valid_neighbors)
        
        local_reqs = distinctify(local_reqs)
        # Remove completed requirements from the current local list of reqs.
        for completed in fulfilled_reqs:
            if completed in local_reqs:
                local_reqs.remove(completed)
        # all_reqs += local_reqs

        # Remove used checks from local checks.
        for completed in placed_checks:
            # del local_checks[completed]
            local_checks.remove(completed)

        # 5. Pick a requirement at random and fulfill it in a random region which does NOT require it.
        local_reqs = random_manager.shuffle_list(local_reqs)
        local_checks = random_manager.shuffle_list(local_checks)

        for current_req in local_reqs:
        # next_hub_available = False
        # while not next_hub_available:
            # Fulfill at least one requirement from the list.
            # current_req = random_manager.get_random_list_member(local_reqs)
            # print(current_req)
            # print(valid_neighbors)

            # for proposed_region in valid_neighbors:
            #     if current_req not in region_map[proposed_region]['requirements']:
            #         return current_req
            use_check = {}
            for check in local_checks:
                if check_is_compatible(current_req, check):
                    use_check = check

            if use_check != {}: # There was at least one compatible check. Proceed.
                if current_req['type'] == 'flag':
                    flag_items = map.FLAGS[current_req['name']]
                    flag_items = random_manager.shuffle_list(flag_items)
                    for item in flag_items:
                        if item not in placed_items:
                            placed_items.append(item)
                            current_req['item'] = item
                            break
                    # Some flag items can fulfill multiple flags.
                    # Cycle through the possible flags based on the item.
                    for alt_flag in map.ITEM_TO_FLAGS[current_req['item']]:
                        flag_req_dict = {'type': 'flag', 'name': alt_flag}
                        if flag_req_dict not in fulfilled_reqs:
                            fulfilled_reqs.append(flag_req_dict)
                    # print(fulfilled_reqs)
                elif current_req['type'] == 'item':
                    placed_items.append(current_req['name'])
                
                use_check.pop('check_requirements')
                spoiler_log.append(
                    {
                        'act': hub['act'],
                        'check': use_check,
                        'requirement': current_req
                    }
                )
            

            # # Returns false if there are no compatible regions. 
            # # Returns a region if there is at least one.
            # target_region = get_compatible_region(current_req, valid_neighbors)
            # if target_region:
            #     compatible_checks = get_compatible_checks(current_req, target_region)
            #     # Make sure there ARE compatible checks
            #     if compatible_checks:
            #         for check in placed_checks:
            #             # print(compatible_checks)
            #             if check in compatible_checks:
            #                 # del compatible_checks[check]
            #                 compatible_checks.remove(check)
            #         print(len(compatible_checks))
            #         print(compatible_checks)
            #         if len(compatible_checks) > 0:
            #             target_check = random_manager.get_random_list_member(compatible_checks)
            #             placed_checks.append(target_check)
            #             fulfilled_reqs.append(current_req)

            #             # Check if this is a flag requirement.
            #             # We need to pick an item that fulfills the flag requirement and place it.
            #             if current_req['type'] == 'flag':
            #                 flag_items = map.FLAGS[current_req['name']]
            #                 flag_items = random_manager.shuffle_list(flag_items)
            #                 for item in flag_items:
            #                     if item not in placed_items:
            #                         placed_items.append(item)
            #                         current_req['item'] = item
            #                         break
            #                 # Some flag items can fulfill multiple flags.
            #                 # Cycle through the possible flags based on the item.
            #                 for alt_flag in map.ITEM_TO_FLAGS[current_req['item']]:
            #                     flag_req_dict = {'type': 'flag', 'name': alt_flag}
            #                     if flag_req_dict not in fulfilled_reqs:
            #                         fulfilled_reqs.append(flag_req_dict)
            #                 # print(fulfilled_reqs)
            #             elif current_req['type'] == 'item':
            #                 placed_items.append(current_req['name'])

            #             spoiler_log.append(
            #                 {
            #                     'check': target_check,
            #                     'requirement': current_req
            #                 }
            #             )

            if all(elem in next_hub_reqs for elem in fulfilled_reqs):
                # next_hub_available = True
                print('Finished placing act:', hub['act'])
                break
            

    return spoiler_log

def check_is_compatible(requirement, check):
    if 'check_requirements' in check and requirement in check['check_requirements']:
        return False
    if requirement['type'] in ['item', 'flag'] and check['type'] in ['chest', 'item']:
        return True 
    elif requirement['type'] in ['npc_id'] and check['type'] in ['lair']:
        return True
    return False

def get_compatible_region(requirement_to_place, region_list):
    for proposed_region in random_manager.shuffle_list(region_list):
        if requirement_to_place not in map.REGIONS[proposed_region]['requirements']:
            return proposed_region

    return False

def get_compatible_checks(requirement_to_place, target_region):
    if requirement_to_place['type'] in ['flag', 'item']:
        target_type = ['item', 'chest']
    elif requirement_to_place['type'] in ['npc_id']:
        target_type = ['lair']
    else:
        return False 

    compatible_checks = []
    for check in map.REGIONS[target_region]['checks']:
        if check['type'] in target_type:
            compatible_checks.append(check)
    
    if len(compatible_checks) > 0:
        return compatible_checks
    return False

# def fulfill_requirement(requirement, target_region_reqs):
#     if requirement not in target_region_reqs:
#         # Loop through checks randomly until a compatible one is found.
#         idx = 0
#         random_check = False
#         while True:
#             # pass
#             random_check = random_manager.get_random_list_member(target_region_reqs['checks'])
#             if random_check['type'] in map.CHECK_TYPE_LOOKUP[requirement['type']]:
#                 break
#             idx += 1
#             if idx >= constants.MAX_LOOPS: 
#                 # After so many loops, we need to break and try a different region.
#                 return False
#         # So far so good.
#         if requirement['type'] == 'npc_id':
#             # pick a lair location from checks.
#             pass 
#         if requirement['type'] == 'item':
#             # Check to see if item already obtained.
#             # If not, pick a chest or item location from checks.
#             # Add item to items allocated list.
#             pass 
#         if requirement['type'] == 'flag':
#             # Check to see if flag already fulfilled
#             # Pick a random item from one of the FLAGS
#             # Put it in a random item or chest location from checks.
#             # Add item to items obtained list.
#             pass
#         else:
#             # No place to put it. Do another loop
#             return False
#     else:
#         return False

#     return True

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
    # neighbor_list should also include self, in case there are unfulfilled reqs there.
    neighbor_list = [node]
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
    output_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'check_spoiler.json')
    with open(output_file, 'w') as f:
        f.write(json.dumps(randomize_result, indent = 4))
    # print(json.dumps(randomize_result, indent = 4))