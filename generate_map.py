import os, json
# import random
import sys, getopt
import networkx as nx
from reference import map, constants, rom_data
import random_manager

valid_args =  "-h        --help                 | Information about the script. \n"
valid_args += "-s <Seed> --seed <Seed>          | The seed used to prime the random number generator. If one is not specified, one will be provided. \n"
valid_args += "-w        --weapon               | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. \n"
valid_args += "-m <ITEM> --magician_item <ITEM> | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. \n"

help_info  = "Help Info: \n"
help_info += "This script handles item placement througout the world. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'seed': None,
        'weapon': False,
        'magician_item': '',
        'debug': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:wm:d',['help','seed=','weapon','magician_item=','debug'])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-s', '--seed'):
            arguments['seed'] = arg.strip()
        elif opt in ('-w', '--weapon'):
            arguments['weapon'] = True
        elif opt in ('-m', '--magician_item'):
            arguments['magician_item'] = arg.strip()
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments
    # End main

def randomize_map(settings={'weapon': False, 'magician_item': '',}):
    debug = False
    if 'debug' in settings and settings['debug']: debug = True
    region_map = map.REGIONS
    region_id_list = list(region_map.keys())
    act_hubs = []

    if debug: print('Starting item randomization...')
    
    # 0. Initialize fulilled requirements and placed items...
    # all_reqs = []
    fulfilled_reqs = []
    placed_checks = []
    # valid_regions = []
    placed_items = []
    spoiler_log = []

    # Starting weapon check.
    sword_of_life_check = map.REGIONS[0]['checks'][0]
    if settings['weapon']: # Randomize the starting weapon
        start_weapon = random_manager.get_random_list_member(map.SWORDS)
        # COME BACK HERE!
        # SET A FLAG IF THE SWORD IS SPECIAL...
        # OR JUST DON"T ALLOW FLAG SWORDS AS STARTERS...
    else:
        start_weapon = map.SWORDS[0] # Sword of Life
    spoiler_log.append(
        {
            'act': 0,
            'check': sword_of_life_check,
            'req': {'type': 'item', 'name': start_weapon}
        }
    )
    placed_items.append(start_weapon)
    placed_checks.append(sword_of_life_check)

    if settings['magician_item'] != '': # Do something I guess
        magician_item_check = map.REGIONS[0]['checks'][1]
        # I don't feel like doing this right now.
        # Check if the magician item is a flag.
        # if it's not a flag, it should be a specific item. 
        # Place the item in the magician spot.
        # Add the requirement based on the item.
        # Add the 

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
    reference_graph = nx.DiGraph()

    # Connect hubs...
    previous_node = None 
    used_regions = []

    # Hubs need to be chronological, not random.
    for hub in act_hubs:
        if previous_node is not None:
            world_graph.add_edge(hub['hub_region'], previous_node['hub_region'])
            reference_graph.add_edge(hub['hub_region'], previous_node['hub_region'])
            pass
        previous_node = hub
        used_regions.append(hub['hub_region'])
        # Connect sub regions for reference graph.
        # Used in determining valid regions later.
        for sub_region in hub['sub_regions']:
            reference_graph.add_edge(hub['hub_region'], sub_region)

    # Randomly connect all other regions...
    for region in region_id_list:
        if region not in used_regions:
            # It's safe to add this region to the network.
            source_node = random_manager.get_random_list_member(used_regions)
            world_graph.add_edge(source_node, region)
            used_regions.append(region)

    # # Connect sub regions to reference graph
    # for region in region_id_list

    # Discover the "next" hub region and record it in the current act.
    # 1. Go to first hub area.
    for hub in act_hubs:
        if debug: print('  Starting act', hub['act'])
        # Determine valid regions
        # 2. Get list of all "connected" regions in the graph to that hub area.
        current_neighbors = get_all_neighbors(world_graph, hub['hub_region'])
        next_hub_reqs = []
        if 'next_hub_region' in hub:
            # 3. Get the 'next' hub region requirements.
            next_hub_reqs = region_map[hub['next_hub_region']]['requirements']

        if debug: print('    Next Hub Requirements:', next_hub_reqs)

        valid_neighbors = []#[hub['hub_region']]
        all_neighbors = get_all_neighbors(reference_graph, hub['hub_region'])
        for neighbor in current_neighbors:
            if neighbor in all_neighbors:
                valid_neighbors.append(neighbor)

        if debug: 
            print('    Valid Neighbor Count:', len(valid_neighbors))
            print('    Valid Neighbor List:', valid_neighbors)

        # 4. Get all known checks and requirements in neighboring regions.
        # We can use requirements from next hub region, but not checks.
        local_reqs = next_hub_reqs 
        local_checks = []
        for local_region in valid_neighbors:
            local_reqs += region_map[local_region]['requirements']
            local_checks += region_map[local_region]['checks']
        
        local_reqs = distinctify(local_reqs)
        # Remove completed requirements from the current local list of reqs.
        for completed in fulfilled_reqs:
            if completed in local_reqs:
                local_reqs.remove(completed)

        # Remove used checks from local checks.
        for completed in placed_checks:
            if completed in local_checks:
                local_checks.remove(completed)

        # 5. Pick a requirement at random and fulfill it in a random region which does NOT require it.
        local_reqs = random_manager.shuffle_list(local_reqs)
        local_checks = random_manager.shuffle_list(local_checks)

        if debug: print('    Total local requirements:', len(local_reqs))

        for current_req in local_reqs:
            if debug: print('      Placing requirement:', current_req)
            # hub_requirements_met = False
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
                if check_is_compatible(current_req, check) and is_check_ok(check, fulfilled_reqs) and check not in placed_checks:
                    use_check = check
                    if debug: print('      In check:', use_check)
                    break

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
                    # Cycle through the possible flags based on the item and "fulfill" as needed.
                    for alt_flag in map.ITEM_TO_FLAGS[current_req['item']]:
                        flag_req_dict = {'type': 'flag', 'name': alt_flag}
                        if flag_req_dict not in fulfilled_reqs:
                            if debug: print('    Alt Flag Enabled:', flag_req_dict)
                            fulfilled_reqs.append(flag_req_dict)
                    # print(fulfilled_reqs)
                elif current_req['type'] == 'item':
                    placed_items.append(current_req['name'])                    
                
                # If the current requirement goes into a check,
                # the check requirements are now also required for next hub access.
                if current_req in next_hub_reqs:
                    # print(current_req)
                    # print(next_hub_reqs)
                    next_hub_reqs += get_check_requirements(use_check)
                    next_hub_reqs = distinctify(next_hub_reqs)

                placed_checks.append(use_check)
                spoiler_log.append(
                    {
                        'act': hub['act'],
                        'check': use_check,
                        'requirement': current_req
                    }
                )

            hub_reqs_met = []
            # print(len(next_hub_reqs))
            for hub_req in next_hub_reqs:
                if hub_req in fulfilled_reqs:
                    hub_reqs_met.append(True)
                else:
                    hub_reqs_met.append(False)
            # print(len(hub_reqs_met))
            # print(all(hub_reqs_met))
            if all(hub_reqs_met):
                # print(next_hub_reqs)
                print('    Hub requirements met')
                # hub_requirements_met = True
                break


            # if all(elem in next_hub_reqs for elem in fulfilled_reqs):
            #     # next_hub_available = True
            #     print('Finished placing act:', hub['act'])
            #     break
        # if hub['act'] == 2: 
        #     print(valid_neighbors)
        #     sys.exit('act 3 start...')
            

    return spoiler_log

# Returns a list of requirements associated with a given check.
def get_check_requirements(check):
    for region_id in map.REGIONS.keys():
        if check in map.REGIONS[region_id]['checks']:
            return map.REGIONS[region_id]['requirements']
    return []

# Returns bool stating that a requirement is compatible with a check or not.
def check_is_compatible(requirement, check):
    if requirement in get_check_requirements(check):
        return False
    if requirement['type'] in ['item', 'flag'] and check['type'] in ['chest', 'item']:
        return True 
    elif requirement['type'] in ['npc_id'] and check['type'] in ['lair']:
        return True
    return False

# Returns bool stating whether a check's requirements are all fulfilled or not.
def is_check_ok(check, fulfilled_reqs):
    completed_reqs = []
    for check_req in get_check_requirements(check):
        if check_req in fulfilled_reqs:
            completed_reqs.append(True)
        else:
            completed_reqs.append(False)
    return all(completed_reqs)


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
    settings_dict = main(sys.argv[1:])
    print('Seed:', settings_dict['seed'])
    print('Randomize Starting Weapon:', settings_dict['weapon'])
    print('Magician Item:', settings_dict['magician_item'])
    print('Debug:', settings_dict['debug'])

    random_manager.start_randomization('hi')
    randomize_result = randomize_map(settings_dict)
    output_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'check_spoiler.json')
    with open(output_file, 'w') as f:
        f.write(json.dumps(randomize_result, indent = 4))
    # print(json.dumps(randomize_result, indent = 4))