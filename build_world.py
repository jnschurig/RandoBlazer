import sys, getopt
import json
import networkx as nx
from reference import map, constants
import random_manager

valid_args = '''Valid Arguments:
-h         --help                   | Information about the script. 
-s <Seed>  --seed <Seed>            | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-a <TYPE>  --world_type <TYPE>      | Determines the method for locating valid places to put checks. Try `--world_type help` for more detail.
# -w <ITEM>  --starting_weapon <ITEM> | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. 
# -m <ITEM>  --magician_item <ITEM>   | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. 
# -t <MODE>  --trash_mode <MODE>      | Determines how trash is dispersed. Default vanilla. Use ''' + str(constants.TRASH_FILL_METHODS) + '''
# -u <ITEMs> --trash <ITEMs>          | A comma separated list (or list object) of all items to be used as trash.
# -p {plan}  --plan {plan}            | A dict or json object with pre-determined placements. Use --plan help for more detail.
# -o         --only_required          | Only add place required key items. Will exclude many swords, most armor, most magic, and goat food. Instead trash items will be placed. 
-g <SCALE> --gem_scaling <SCALE>    | Multiply the gem/exp amounts from chests and NPCs by the input scale. Default 1 (gives vanilla gem amounts).
-z         --randomize_hubs         | Randomize the world hub placement. Not implemented
'''

help_info = '''Help Info: 

Uses network graph logic to control which areas of the game can have progression at a given point in time.
- **Vanilla**  - All regions in an act can have logical progression.
- **Balanced** - Sub-regions will be randomly connected to hub-regions. As a result, some regions will be 
                 excluded from having your current logical progression. However, there may be later-required 
                 progression in a region that could be excluded from current progression.
- **Advanced** - Sub-regions are randomly connected to any other already-connected region. Progression logic 
                 is the Same as in "balanced", but there is a higher likelihood of having entirely "dead" 
                 regions that have no progression whatsoever. This mode is more likely to reward skipping 
                 regions.
'''

def main(argv):
    arguments = {
        'seed': None,
        'world_type': 'vanilla',
        # 'starting_weapon': 'SWORD_OF_LIFE',
        # 'magician_item': 'RANDOM',
        # 'trash_mode': 'vanilla',
        # 'trash': [],
        # 'plan': [],
        # 'only_required': False, 
        # 'randomize_hubs': False, # Not an implemented feature yet...
        # 'gem_scaling': 1, 
        'debug': False,
        'verbose': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:w:m:a:t:u:p:ozg:dv',['help','seed=','starting_weapon=','magician_item=','world_type=','trash_mode=','trash=','plan=','only_required','randomize_hubs','gem_scaling=','debug','verbose'])
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
        elif opt in ('-a', '--world_type'):
            arguments['world_type'] = arg.strip().lower()
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
        elif opt in ('-v', '--verbose'):
            arguments['verbose'] = True
    
    if False: print(args) # Thanks, I hate it.

    # if type(arguments['plan']) is str and arguments['plan'].strip().lower() == 'help':
    #     print(plan_help)
    #     sys.exit(2)

    # if arguments['world_type'].lower() == 'help':
    #     print(world_type_help)
    #     sys.exit(1)

    # if arguments['world_type'] not in constants.VALID_WORLD_TYPES:
    #     print('Selected world type:', arguments['world_type'])
    #     print('Valid world types:', constants.VALID_WORLD_TYPES)
    #     print('Try --world_type help for additional detail.')
    #     sys.exit(2)

    # if arguments['starting_weapon'].lower() == 'help':
    #     print(starting_weapon_help)
    #     sys.exit(1)

    # if arguments['starting_weapon'] not in map.SWORDS + ['RANDOM']:
    #     print('Selected starting weapon:', arguments['starting_weapon'])
    #     print('Valid starting weapons:', map.SWORDS)
    #     print('Try --starting_weapon help for additional detail.')
    #     sys.exit(2)

    # if arguments['magician_item'].lower() == 'help':
    #     print(magician_item_help)
    #     sys.exit(1)

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

def initialize_world(settings={'world_type': 'vanilla'}):
    '''
    Takes a settings dict with 'world_type' key and generates 
    a graph based on that setting. As of this writing, valid 
    settings are vanilla, balanced, and advanced. Returns a 
    networkx digraph object. See help_info in same script 
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

if __name__ == '__main__':
    settings_dict = main(sys.argv[1:])
    settings_dict['seed'] = random_manager.start_randomization(settings_dict['seed'])
    world_graph = initialize_world(settings_dict)
    print(world_graph.nodes())
