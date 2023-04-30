import sys, getopt

from reference import map 

valid_args = '''Valid Arguments:
-h         --help                   | Information about the script. 
-s <Seed>  --seed <Seed>            | The seed used to prime the random number generator. If one is not specified, one will be provided. 
-a <TYPE>  --world_type <TYPE>      | Determines the method for locating valid places to put checks. Try `--world_type help` for more detail.
# -w <ITEM>  --starting_weapon <ITEM> | Randomize starting weapon. If set, a random sword will be in the starting chest. Otherwise it will be Sword of Life. 
# -m <ITEM>  --magician_item <ITEM>   | Choose what the magician will drop. Use 'has_magic' for a random spell. Leave blank for random item. 
# -u <ITEMs> --trash <ITEMs>          | A comma separated list (or list object) of all items to be used as trash.
# -p {plan}  --plan {plan}            | A dict or json object with pre-determined placements. Use --plan help for more detail.
# -o         --only_required          | Only add place required key items. Will exclude many swords, most armor, most magic, and goat food. Instead trash items will be placed. 
-g <SCALE> --gem_scaling <SCALE>    | Multiply the gem/exp amounts from chests and NPCs by the input scale. Default 1 (gives vanilla gem amounts).
-z         --randomize_hubs         | Randomize the world hub placement. Not implemented
'''

help_info = '''Help Info: 

This script handles item placement througout the world. 
The arguments are intended to be used for testing by running this script all by itself. 
The networkx package is in use to assist with graph creation and traversal. 
'''

def go(nx_digraph, placement_dict={}):

    return {}

if __name__ == '__main__':

    go()