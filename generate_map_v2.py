import sys, getopt
import os, json
import networkx as nx
from reference import map, constants, rom_data
import random_manager

valid_args = """Valid Arguments:
-h         --help                 | Information about the script. 
-s <Seed>  --seed <Seed>          | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-w         --weapon               | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. 
-m <ITEM>  --magician_item <ITEM> | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. 
-a         --advanced_world       | Uses graph logic to eliminate certain areas from having early require progression. 
-t <ITEM>  --all_trash <ITEM>     | Replaces all optional items with the trash item of your choosing. 
-g         --random_gem_amounts   | Randomize the gem amounts on the gem/xp checks. 
-p {plan}  --plan {plan}          | A dict or json object with pre-determined placements. Use --plan help for more detail.
-o         --randbomize_hubs      | Randomize the world hub placement. Not implemented
"""

help_info = """Help Info: 
This script handles item placement througout the world. 
The arguments are intended to be used for testing by running this script all by itself. 
The networkx package is in use to assist with graph creation and traversal. 
"""

plan_help = '''Plan Help:
Here I will put more detail regarding how to pre-place whatever. For choosing beginning 
weapon or magician item, use --weapon or --magician_item.
'''

def main(argv):
    arguments = {
        'seed': None,
        'weapon': False,
        'magician_item': '',
        'advanced_world': False,
        'all_trash': '',
        'plan': {},
        'randbomize_hubs': False,
        'debug': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:wm:at:p:od',['help','seed=','weapon','magician_item=','advanced_world','all_trash=','plan=','randbomize_hubs','debug'])
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
        elif opt in ('-a', '--advanced_world'):
            arguments['advanced_world'] = True
        elif opt in ('-t', '--all_trash'):
            arguments['all_trash'] = arg.strip()
        elif opt in ('-p', '--plan'):
            arguments['plan'] = arg
        elif opt in ('-o', '--randbomize_hubs'):
            arguments['randbomize_hubs'] = True
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: print(args) # Thanks, I hate it.

    if type(arguments['plan']) is str and arguments['plan'].strip() == 'help':
        print(plan_help)
        sys.exit()

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
    
def randomize_map(settings={'weapon': False, 'magician_item': '','advanced_world': True}):
    debug = False
    if 'debug' in settings and settings['debug']: debug = True 

    if debug: print('Starting item randomization...')
    region_map = map.REGIONS
    region_id_list = list(region_map.keys())
    act_hubs = []

    # 0. Initialize fulilled requirements and placed items...
    # fulfilled_reqs = []
    # placed_checks = []
    # placed_items = []
    # spoiler_log = []

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
        # reference_graph = world_graph
        for sub_region in hub['sub_regions']:
            reference_graph.add_edge(hub['hub_region'], sub_region)

    # In the event we do an "advanced" world.
    if settings['advanced_world']:
        # Randomly connect all other regions...
        for region in region_id_list:
            if region not in used_regions: # It's safe to add this region to the network.
                source_node = random_manager.get_random_list_member(used_regions)
                world_graph.add_edge(source_node, region)
                used_regions.append(region)
    else:
        world_graph = reference_graph

    return world_graph

if __name__ == '__main__':
    settings_dict = main(sys.argv[1:])
    settings_dict['seed'] = random_manager.start_randomization(settings_dict['seed'])
    print('Seed:', settings_dict['seed'])
    print('Randomize Starting Weapon:', settings_dict['weapon'])
    print('Magician Item:', settings_dict['magician_item'])
    print('Advanced World:', settings_dict['advanced_world'])
    print('Debug:', settings_dict['debug'])

    randomize_result = randomize_map(settings_dict)
    output_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'check_spoiler.json')
    with open(output_file, 'w') as f:
        f.write(json.dumps(randomize_result, indent = 4))
    # print(json.dumps(randomize_result, indent = 4))