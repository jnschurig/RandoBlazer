import sys, getopt
import json, os
import networkx as nx
from reference import map, constants, rom_data
import random_manager

valid_args = '''Valid Arguments:
-h         --help                   | Information about the script. 
-s <Seed>  --seed <Seed>            | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-w <ITEM>  --starting_weapon <ITEM> | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. 
-m <ITEM>  --magician_item <ITEM>   | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. 
-a         --world_type             | Determines the method for locating valid places to put checks. See
-t <ITEM>  --trash <ITEM>           | Replaces all optional items with the trash item of your choosing. 
-g         --random_gem_amounts     | Randomize the gem amounts on the gem/xp checks. 
-p {plan}  --plan {plan}            | A dict or json object with pre-determined placements. Use --plan help for more detail.
-o         --randbomize_hubs        | Randomize the world hub placement. Not implemented
'''

help_info = '''Help Info: 
This script handles item placement througout the world. 
The arguments are intended to be used for testing by running this script all by itself. 
The networkx package is in use to assist with graph creation and traversal. 
'''

plan_help = '''Plan Help:
Here I will put more detail regarding how to pre-place whatever. For choosing beginning 
weapon or magician item, use --starting_weapon or --magician_item.
'''

world_type_help = '''World Type Help:
Uses graph logic to control which areas of the game can having progression at a given point in time.
- vanilla  - All regions in an act can have logical progression.
- balanced - Some regions will be excluded from having your current logical progression. However, there 
             may be later-required progression in a region that could be excluded from current progression.
- Advanced - Same as balanced, but there is a higher likelihood of having entirely "dead" regions that have 
             no progression whatsoever.
'''

starting_weapon_help = '''Starting Weapon Help
Determine the starting weapon in the first chest of the game.
Default: SWORD_OF_LIFE (Sword of Life)
Valid options are any of the swords in the game or "random"
Valid swords:''' + str(map.SWORDS) + ''' 
'''

magician_item_help = '''Magician Item Help
Determine the second item in the game as given by the magician. In the vanilla game this would be the 
fireball magic. 
Default: random
Valid items include:
RANDOM
'''
# mag_item_list = []
for ref_item in rom_data.ITEMS.keys():
    magician_item_help += ref_item + ' \n'
    # mag_item_list.append(ref_item)
del ref_item

def main(argv):
    arguments = {
        'seed': None,
        'starting_weapon': 'SWORD_OF_LIFE',
        'magician_item': 'RANDOM',
        'world_type': 'vanilla',
        'trash': 'vanilla',
        'plan': [],
        'randbomize_hubs': False, # Not an implemented feature yet...
        'debug': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:wm:a:t:p:od',['help','seed=','starting_weapon=','magician_item=','world_type=','trash=','plan=','randbomize_hubs','debug'])
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
        elif opt in ('-w', '--starting_weapon'):
            arguments['starting_weapon'] = arg.strip().upper()
        elif opt in ('-m', '--magician_item'):
            arguments['magician_item'] = arg.strip().upper()
        elif opt in ('-a', '--world_type'):
            arguments['world_type'] = arg.strip().lower()
        elif opt in ('-t', '--trash'):
            arguments['trash'] = arg.strip().upper()
        elif opt in ('-p', '--plan'):
            arguments['plan'] = arg
        elif opt in ('-o', '--randbomize_hubs'):
            arguments['randbomize_hubs'] = True
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: print(args) # Thanks, I hate it.

    if type(arguments['plan']) is str and arguments['plan'].strip().lower() == 'help':
        print(plan_help)
        sys.exit(2)

    if arguments['world_type'].lower() == 'help':
        print(world_type_help)
        sys.exit(1)

    if arguments['world_type'] not in constants.VALID_WORLD_TYPES:
        print('Selected world type:', arguments['world_type'])
        print('Valid world types:', constants.VALID_WORLD_TYPES)
        print('Try --world_type help for additional detail.')
        sys.exit(2)

    if arguments['starting_weapon'].lower() == 'help':
        print(starting_weapon_help)
        sys.exit(1)

    if arguments['starting_weapon'] not in map.SWORDS + ['RANDOM']:
        print('Selected starting weapon:', arguments['starting_weapon'])
        print('Valid starting weapons:', map.SWORDS)
        print('Try --starting_weapon help for additional detail.')
        sys.exit(2)

    if arguments['magician_item'].lower() == 'help':
        print(magician_item_help)
        sys.exit(1)

    return arguments
    # End main

# Input a list which may or may not be unique.
# Output a list which is definitely unique.
# If input is not a list type, return the same thing without changes.
def distinctify(non_unique_list):
    '''
    Takes a list object as input and returns a list containing 
    only unique items from the original list.

    Example:
    input list: [1, 2, 3, 4, 5, 1, 2]
    output list: [1, 2, 3, 4, 5]
    '''
    if type(non_unique_list) is not list:
        return non_unique_list
    
    unique_list = []
    for item in non_unique_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    
def get_all_neighbors(graph, node):
    # neighbor_list should also include self, in case there are unfulfilled reqs there.
    '''
    Takes a networkx graph and one of its nodes as input. 
    Returns a list containing all neighboring nodes, including 
    node specified in the input. In a digraph type, it will respect 
    directional relationships and not go "upstream".

    Graph example 6 -> 0 -> 1
                         -> 2
                         -> 3

    graph: (see above)
    input node: 0 
    returns: [0, 1, 2, 3]

    input node: 6 
    returns: [6, 0, 1, 2, 3]

    node: 2
    returns: [2]

    '''
    neighbor_list = [node]
    for neighbor in graph.neighbors(node):
        neighbor_list.append(neighbor)
        neighbor_list += get_all_neighbors(graph, neighbor)
    return distinctify(neighbor_list)

def item_to_flag_reqs(item_name):
    '''
    Takes an item)id as defined in the key values of 
    rom_data.ITEMS.keys() and returns a list of any 
    flags that might be associated with that item.

    input: foo
    return: []

    input: SOUL_BLADE
    return: ['can_cut_metal', 'has_thunder', 'can_cut_spirit']

    input: MEDICAL_HERB
    return: []
    '''
    if item_name in map.ITEM_TO_FLAGS:
        return map.ITEM_TO_FLAGS[item_name]
    return []

def get_hub_by_act(act_num):
    '''
    Input an act number and get its hub's region id.
    Returns false if none could be found.
    Example:
    input -> 1
    return -> 0

    input -> 2
    return -> 6

    input -> 3
    return -> 12
    '''
    for region in map.REGIONS:
        if 'is_act_hub' in map.REGIONS[region] and map.REGIONS[region]['act'] == act_num:
            return region

    return False

def get_next_hub(world_graph, hub=0):
    ''' 
    Returns the next hub above the input hub. This assumes
    that hubs descend from each other with 7 as the first, 
    and that sub regions descend from hubs. If multiple 
    parents exist, it will return the first match.

    This is its own function because it requires backwards 
    digraph traversal.
    Graph example 6 -> 0 -> 1
                         -> 2
                         -> 3

    world_graph: (see above)
    child: 0 
    returns: [6]

    world_graph: (see above)
    child: 2
    returns: [0]
    '''

    for x in nx.all_neighbors(world_graph, hub):
        if x not in nx.neighbors(world_graph, hub):
            return x

    return hub

# def collapse_region_checks(world_graph, node):
#     # First get all the neighbors
#     all_checks = []
#     for region in get_all_neighbors(world_graph, node):
#         for check in map.REGIONS[region]['checks']:
#             check['requirements'] = map.REGIONS[region]['requirements']
#             all_checks.append(check)

#     return all_checks

def check_is_compatible(location, requirement):
    '''
    Takes a location or 'check' input and requirement 
    and determines if they are compatible with each 
    other. The location and requirement should be 
    formatted exactly like the map.REGIONS checks and 
    requirements that are found there.
    Returns boolean True or False.
    '''
    if requirement['type'] == 'item' and location['type'] in ['chest', 'item']:
        return True 
    elif requirement['type'] == 'npc_id' and location['type'] == 'lair':
        return True

    return False

def initialize_world(settings={'world_type': 'vanilla'}):
    '''
    Takes a settings dict with 'world_type' key and generates 
    a graph based on that setting. As of this writing, valid 
    settings are vanilla, balanced, and advanced. Returns a 
    networkx digraph object. See world_type_help in same script 
    for additional detail.
    '''
    debug = False
    if 'debug' in settings and settings['debug']: 
        debug = True 
        print(json.dumps(settings, indent = 4))

    if debug: print('Building world...')
    world_graph = nx.DiGraph()

    # Steps
    # 1. Get a LIST of hub region_ids.
    hub_regions = []
    # 2. Get a LIST of sub region_ids. 
    sub_regions = []
    for region_id in map.REGIONS.keys():
        if 'is_act_hub' in map.REGIONS[region_id] and map.REGIONS[region_id]['is_act_hub']:
            hub_regions.append(region_id)
        else:
            sub_regions.append(region_id)
    del region_id

    # 3. Add the regions 
    previous_hub = -1 # a non-existent hub id that is less than 0
    for hub_id in hub_regions:
        if previous_hub >= 0:
            world_graph.add_edge(hub_id, previous_hub)
            if debug: print('Edge:', hub_id, '->', previous_hub)
        previous_hub = hub_id
    del hub_id
    del previous_hub

    if settings['world_type'] == 'vanilla':
        # a. In a vanilla world, connect all regions to their parent hub
        for hub_id in hub_regions:
            act_number = map.REGIONS[hub_id]['act']
            previous_id = hub_id
            for sub_id in sub_regions:
                if map.REGIONS[sub_id]['act'] == act_number:
                    world_graph.add_edge(previous_id, sub_id)
                    previous_id = sub_id
            del sub_id
        del hub_id

    if settings['world_type'] == 'balanced':
        # b. In balanced world, tie each sub region to a random hub
        for sub_id in sub_regions:
            random_hub = random_manager.get_random_list_member(hub_regions)
            world_graph.add_edge(random_hub, sub_id)
        del sub_id
        del random_hub

    if settings['world_type'] == 'advanced':
        # c. In advanced world, randomly tie each sub region to any other placed region (parent or sub)
        placed_regions = hub_regions
        for sub_id in sub_regions:
            random_parent = random_manager.get_random_list_member(placed_regions)
            world_graph.add_edge(random_parent, sub_id)
            placed_regions.append(sub_id)
        del sub_id
        del random_parent
        del placed_regions
        
    # 4. Add the DATA from the actual regions as an attribute of each node
    #   a. iterate through the nodes and add the region info based on the region id.


    if debug:
        print('Total regions:', len(map.REGIONS.keys()))
        print('Placed regions:', nx.number_of_nodes(world_graph))
        print('Hub Regions:', hub_regions)
        print('All Nodes:', nx.nodes(world_graph))

    return world_graph

def randomize_items(world_graph, settings_dict={'starting_weapon': 'SWORD_OF_LIFE', 'magician_item': 'RANDOM', 'trash': 'VANILLA'}):
    '''
    Takes a networkx digraph object as generated by initialize_world() 
    and a settings dict with a minimum of settings: 'starting_weapon', 
    'magician_item', and 'trash', and randomly assigns items and npcs 
    to the locations specified in map.REGIONS. Returns a json object 
    structured like this:
    {
        '0': [list of checks and locations],
        '1': [list of checks and locations],
        ...
        '7': [list of checks and locations],
    }
    Additional keys may be added to track trash and enemy placement.
    '''
    debug = False 
    if 'debug' in settings_dict and settings_dict['debug']:
        debug = True
        print(json.dumps(settings_dict, indent = 4))
    # Initialize states
    placed_checks = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        # 'trash': [],
    }

    if debug:
        print('Initializing variables...')
    placed_locations = []
    fulfilled_requirements = []
    all_requirements = []
    all_check_locations = []
    for region in map.REGIONS.keys():
        all_check_locations += map.REGIONS[region]['checks']
        for req in map.REGIONS[region]['requirements']:
            if req['type'] != 'flag':
                all_requirements.append(req)
    del region
    if debug: print('all_check_locations: DONE')
    all_requirements = distinctify(all_requirements)
    if debug: print('all_requirements: DONE')
    key_items_to_place = []
    if debug: print('Gathering key items...')
    for key_item in map.KEY_ITEMS:
        key_items_to_place.append({'type': 'item', 'name': key_item})
    del key_item
    if debug: print('DONE')

    if debug: print('Gathering key NPCs...')
    for key_npc in map.NPC_ID.keys():
        key_items_to_place.append({'type': 'npc_id', 'name': key_npc})
    del key_npc
    if debug: print('DONE')

    key_items_to_place = random_manager.shuffle_list(key_items_to_place)
    plan = []

    # Specific functions for item randomization section.
    def get_placements():
        '''
        Returns a flat list of all placement json objects.
        See place_check() for an example of a placement 
        json object.

        This function should only be used within the 
        context of the parent function
        '''
        placements = []
        for key in placed_checks.keys():
            placements += placed_checks[key]

        return placements

    def place_check(placement_dict):
        ''' 
        Places an item or npc and appends all the correct lists.
        A placement dict will look like this:
        {
            'act': 1, # (exclusively 1-7)
            'location': {'type': 'chest', 'id': 0}, # (as seen in map.REGIONS under "checks")
            'placement': {'type': 'npc_id', 'name': 'NPC_BRIDGE_GUARD'} # (as seen in map.REGEIONS under "requirements")
        }

        This function should only be used within the 
        context of the parent function
        '''
        act_number = placement_dict['act']
        del placement_dict['act']

        for alt_flag in item_to_flag_reqs(placement_dict['placement']['name']):
            flag_dict = {'type': 'flag', 'name': alt_flag}
            if flag_dict not in fulfilled_requirements:
                fulfilled_requirements.append({'type': 'flag', 'name': alt_flag})

        if placement_dict['placement'] not in fulfilled_requirements:
            fulfilled_requirements.append(placement_dict['placement'])

        # Pretty up the chest name...
        if placement_dict['location']['type'] == 'chest' and 'name' not in placement_dict['location']:
            placement_dict['location']['name'] = map.CHEST_ITEMS[placement_dict['location']['id']]['item_id']

        placed_checks[act_number].append(placement_dict)
        placed_locations.append(placement_dict['location'])
        return True

    def unplace_act(act):
        '''
        Resets the state of placed checks in an act. This is done to 
        prevent a deadlock where non-essential checks get made, 
        filling all the spots for essential ones. Flag-based ones 
        and next hub requirement ones do not get reset.
        '''
        if act in placed_checks:
            placements_to_remove = []
            next_hub = get_next_hub(world_graph, get_hub_by_act(act))
            for placement in placed_checks[act]:
                if placement['placement']['type'] == 'item' and item_to_flag_reqs(placement['placement']['name']):
                    # This logic states that if the type is an item 
                    # and the item is related to flags, do nothing
                    pass
                elif placement['placement']['type'] == 'npc_id' and placement['placement'] in map.REGIONS[next_hub]['requirements']:
                    # Check to see if the npc is one of the 
                    # required ones for the next hub.
                    # If so, do nothing.
                    pass
                else:
                    # destroy that placement...
                    placements_to_remove.append(placement)
            
            for removal in placements_to_remove:
                placed_checks[act].remove(removal)
                if removal['location'] in placed_locations:
                    placed_locations.remove(removal['location'])
                if removal['placement'] in fulfilled_requirements:
                    fulfilled_requirements.remove(removal['placement'])
            return True
        return False

    # Do starting weapon...
    if debug: print('Placing starting_weapon...')
    if settings_dict['starting_weapon'] == 'RANDOM':
        settings_dict['starting_weapon'] = random_manager.get_random_list_member(map.SWORDS)

    plan_member_sol = {
        'act': 0,
        'location': map.REGIONS[0]['checks'][0],
        'placement': {'type': 'item', 'name': settings_dict['starting_weapon']}
    }
    plan.append(plan_member_sol)
    if debug: print('DONE')
    
    # key_items_to_place.remove(settings_dict['starting_weapon'])

    if settings_dict['magician_item'] != 'RANDOM':
        if debug: print('Placing magician_item...')
        # Take the item setting and add it to the plan
        plan_member_mag_item = {
            'act': 0,
            'location': map.REGIONS[0]['checks'][1],
            'placement': {'type': 'item', 'name': settings_dict['magician_item']}
        }
        plan.append(plan_member_mag_item)
        if debug: print('DONE')

    if 'plan' in settings_dict:
        plan += list(settings_dict['plan'])

    if debug: print('Placing plan_members:', len(plan))
    for plan_member in plan:
        place_check(plan_member)
    del plan_member
    if debug: print('DONE')


    def get_local_requirements(hub_region):
        '''
        Takes a node id as input and returns the non-fullfilled 
        requirements associated with that node and all neighbors.
        Also includes requirements for the parent node that is 
        "upstream" one position in the digraph.

        This was intended to be used with hub regions, but the 
        function will still work just fine with any node in the 
        graph.
        '''
        
        # Get a list of valid regions, then gather up all 
        valid_regions = [get_next_hub(world_graph, hub_region)]
        all_neighbors = get_all_neighbors(world_graph, hub_region)
        for region_id in all_neighbors:
            if 'is_act_hub' in map.REGIONS[region_id]:
                valid_regions.append(region_id)
                for sub_region in map.REGIONS[region_id]['connected_regions']:
                    if sub_region in all_neighbors:
                        valid_regions.append(sub_region)

        # the possible placements (requirements) for those regions
        valid_requirements = []
        for valid_id in valid_regions:
            for req in map.REGIONS[valid_id]['requirements']:
                if req not in fulfilled_requirements:
                    valid_requirements.append(req)

        return distinctify(valid_requirements)

    def get_local_locations(hub_region):
        '''
        Takes a hub region (again, doesn't have to be a hub) 
        and returns all checks (or locations) that are not 
        already placed that are also logically available 
        based on already fulfilled requirements.
        '''
        # Get a list of regions (not including anything upstream)
        valid_regions = []
        all_neighbors = get_all_neighbors(world_graph, hub_region)
        for region_id in all_neighbors:
            if 'is_act_hub' in map.REGIONS[region_id]:
                valid_regions.append(region_id)
                for sub_region in map.REGIONS[region_id]['connected_regions']:
                    if sub_region in all_neighbors:
                        valid_regions.append(sub_region)

        # Get a list of checks that are currently compatible with the world 
        # and with the list of fulfilled requirements.
        valid_locations = []
        for valid_id in valid_regions:
            region_is_ok = True
            for region_req in map.REGIONS[valid_id]['requirements']:
                if region_req not in fulfilled_requirements:
                    region_is_ok = False 
                    break 
            if region_is_ok:
                valid_locations += map.REGIONS[valid_id]['checks']

        # Make sure each check/location is not already placed.
        return_locations = []
        for loc in valid_locations:
            if loc not in placed_locations:
                return_locations.append(loc)

        return distinctify(return_locations)

    def region_requirements_fulfilled(region_id):
        '''
        Returns True if all requirements in a region 
        have been met in fulfilled_requirements[].
        Returns False if not.
        '''
        if 'requirements' in map.REGIONS[region_id]:
            for req in map.REGIONS[region_id]['requirements']:
                if req not in fulfilled_requirements:
                    return False
            return True
        return False

    current_hub = 0
    current_act = map.REGIONS[current_hub]['act']
    # debug_req = json.loads('{"type": "npc_id", "name": "NPC_VILLAGE_CHIEF"}')
    # debug_locations = get_local_locations(current_hub)
    # print(len(debug_locations))
    # print(json.dumps(debug_locations))
    # debug_locations = random_manager.shuffle_list(debug_locations)
    # print(len(debug_locations))
    # print(json.dumps(debug_locations))

    # sys.exit('TESTING')

    # Now we need to do the following:
    # 1. We need to compile a list of available placemenets (requirements) (items and npcs)
    #    this list may be customized at some point based on input. For now it includes everything...
    #   a. Start a loop and iterate until complete...
    if debug: 
        print('Starting full randomization...')
        print('Act:', current_act)

    total_restarts = 0
    region_restarts = 0
    while len(get_placements()) < len(all_requirements):
        # idx += 1
        next_hub = get_next_hub(world_graph, current_hub)
        if region_restarts >= constants.MAX_LOOPS:
            print('ERROR: maximum region re-rolls reached. There is an issue with the logic...')
            sys.exit(2)
        # 2. get a list of requirements we need to fulfill
        next_requirement = random_manager.get_random_list_member(get_local_requirements(current_hub))
        # if debug: print('next_requirement:', json.dumps(next_requirement))
        # Is next requirement a flag? if so, choose a random item to fullfill it.
        is_flag = False
        if next_requirement and next_requirement['type'] == 'flag':
            is_flag = True
            # if debug: print('next requirement is a flag...')
            actual_item = random_manager.get_random_list_member(map.FLAGS[next_requirement['name']])
            flag_requirement = next_requirement
            next_requirement = {'type': 'item', 'name': actual_item}
        possible_locations = random_manager.shuffle_list(get_local_locations(current_hub))
        # if debug: print('possible_locations:', json.dumps(possible_locations))
        
        placed_check_count = len(placed_locations)
        for use_loc in possible_locations:
            if check_is_compatible(use_loc, next_requirement):
                # Place that check.
                placement = {
                    'act': current_act,
                    'location': use_loc,
                    'placement': next_requirement,
                }
                place_check(placement)
                if is_flag:
                    fulfilled_requirements.append(flag_requirement)
                break

        if len(placed_locations) == placed_check_count:
            # We couldn't place a thing, so there was no place for it.
            # Let's reset some checks and try the randomization again.
            if debug:
                print('Unplacing act checks...')

            # Possibly need to pick a "next hub" requirement to fulfill.
            # For now just rerolling the rng seems to work.
            unplace_act(current_act)
            region_restarts += 1


        if region_requirements_fulfilled(next_hub):
            current_hub = next_hub
            current_act = map.REGIONS[current_hub]['act']
            total_restarts += region_restarts
            region_restarts = 0

            # if debug: 
            #     print('Act:', current_act)
                # print('Checks placed:', len(placed_locations))
    print('Total Restarts:', total_restarts)

    # Now time to dole out the "trash"
    # Save this for another time I think.

    if debug:
        print('Total Requirements:', len(all_requirements), '(no flag items)')
        print('Actual Requirements Fulfilled:', len(fulfilled_requirements), '(includes flags and flag items)')
        print('Placed Check Locations:', len(get_placements()))
        print('Total Check Locations:', len(all_check_locations))
        print('Remaining Locations to Populate:', len(all_check_locations) - len(get_placements()))

    return placed_checks

if __name__ == '__main__':
    settings_dict = main(sys.argv[1:])
    settings_dict['seed'] = random_manager.start_randomization(settings_dict['seed'])
    print('Seed:', settings_dict['seed'])
    print('Starting Weapon:', settings_dict['starting_weapon'])
    print('Magician Item:', settings_dict['magician_item'])
    print('World Type:', settings_dict['world_type'])
    print('Debug:', settings_dict['debug'])

    world_graph = initialize_world(settings_dict)
    randomization = randomize_items(world_graph, settings_dict)

    output_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'check_spoiler.json')
    with open(output_file, 'w') as f:
        f.write(json.dumps(randomization, indent = 4))
    # print(json.dumps(randomize_result, indent = 4))