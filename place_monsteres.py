import os, sys, getopt
import random_manager

valid_args =  "-h        --help        | Information about the script. \n"
valid_args += "-s <Seed> --seed <Seed> | The seed used to prime the random number generator. If one is not specified, one will be provided. \n"
valid_args += "-x        --cross_act   | Allow monsters to be randomized across different acts. \n"
valid_args += "-n        --non_random  | Do not randomize monster lairs. \n"

help_info  = "Help Info: \n"
help_info += "This script will modify the contents ROM data and replace bits of it with other data. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'seed': None,
        'cross_act': False,
        'debug': False,
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:xd',['help','seed=','cross_act','debug'])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-s', '--seed'):
            arguments['seed'] = arg
        elif opt in ('-x', '--cross_act'):
            arguments['cross_act'] = True
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments

def randomize_lair_monsters(settings_dict):
    debug = False
    if 'debug' in settings_dict and settings_dict['debug']: debug = True
    spoiler_log = []
    '''
    pseudo code
    if lair type is two_up_two_down: 
        don't randomize
    if lair type is MustNotRandomizeLairPosition:
        don't randomize

    cycle through acts...
    Should we have an option to randomize enemies across acts? Yes. Let's build that in.
    randomize enemy 
    randomize direction
        Some cannot be in certain orientations
            No up
    randomize spawn type
        LAIR_ONE_BY_ONE
        LAIR_MULTISPAWN
        LAIR_ONE_BY_ONE_PROX
    randomize spawn amount
    '''

    return spoiler_log

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])

