# from asyncio import constants
import sys, getopt
# import os, json
import networkx as nx
# from numpy import source
from reference import map, constants, rom_data
import random_manager

valid_args = '''Valid Arguments:
-h         --help                   | Information about the script. 
-s <Seed>  --seed <Seed>            | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-w <ITEM>  --starting_weapon <ITEM> | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. 
-m <ITEM>  --magician_item <ITEM>   | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. 
-a         --world_type             | Determines the method for locating valid places to put checks. See
-t <ITEM>  --all_trash <ITEM>       | Replaces all optional items with the trash item of your choosing. 
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
random
'''
for ref_item in rom_data.ITEMS.keys():
    magician_item_help += ref_item + ' \n'
del ref_item

def main(argv):
    arguments = {
        'seed': None,
        'starting_weapon': 'SWORD_OF_LIFE',
        'magician_item': 'RANDOM',
        'world_type': 'vanilla',
        'all_trash': '',
        'plan': {},
        'randbomize_hubs': False, # Not an implemented feature yet...
        'debug': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:wm:a:t:p:od',['help','seed=','starting_weapon=','magician_item=','world_type=','all_trash=','plan=','randbomize_hubs','debug'])
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
        elif opt in ('-t', '--all_trash'):
            arguments['all_trash'] = arg.strip().upper()
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

    if arguments['magician_item'] != 'RANDOM' or arguments['magician_item'] not in list(rom_data.ITEMS.keys()) + ['RANDOM']:
        print('Selected magician item: "' + arguments['magician_item'] + '" is invalid.')
        print('Try --magician_item help for additional detail.')
        sys.exit(2)

    return arguments
    # End main

# Input a list which may or may not be unique.
# Output a list which is definitely unique.
# If input is not a list type, return the same thing without changes.
def distinctify(non_unique_list):
    if type(non_unique_list) is not list:
        return non_unique_list
    
    unique_list = []
    for item in non_unique_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    
def initialize_world(settings={'world_type': 'vanilla'}):
    debug = False
    if 'debug' in settings and settings['debug']: debug = True 

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
    previous_hub = -1
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

def randomize_items(world_graph, settings_dict={'starting_weapon': 'SWORD_OF_LIFE', 'magician_item': 'random'}):


    return True

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

    # randomize_result = randomize_map(settings_dict)
    # output_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'check_spoiler.json')
    # with open(output_file, 'w') as f:
    #     f.write(json.dumps(randomize_result, indent = 4))
    # print(json.dumps(randomize_result, indent = 4))