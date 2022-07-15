import sys, getopt
import random
from reference import constants

valid_args =  "-h        --help        | Information about the script. \n"
valid_args += "-s <Seed> --seed <Seed> | The seed used to prime the random number generator. If one is not specified, one will be provided. \n"

help_info  = "Help Info: \n"
help_info += "This script will return any needed random values. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'seed': None
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hs:',['help','seed='])
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
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments
    # End main

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def number_list_to_str(num_list):
    new_num = ''
    for val in num_list:
        new_num += constants.BASE_LOOKUP[val]

    return new_num

def start_randomization(seed_value=None):
    if seed_value == None or seed_value == '':
        seed_int = random.randint(constants.SEED_MIN, constants.SEED_MAX)
        seed_value = number_list_to_str(number_to_base(seed_int, constants.SEED_BASE))

    random.seed(seed_value)

    return seed_value

def get_random_int(min=0, max=None):
    # Returns a random integer between the min and max
    # If the min is greater than the max, the values are reversed.
    if max == None:
        max = constants.DEFAULT_RANDOM_MAX_INT
    
    if min > max:
        temp = min
        min = max
        max = temp

    return random.randint(int(min), int(max))

def get_random_list_member(list_values):
    if len(list_values) == 0:
        return None
    return list_values[get_random_int(1, len(list_values)) - 1]

def shuffle_list(ordered_list=[]):
    # Returns a new, shuffled list, leaving the original order intact.
    new_list = ordered_list
    random.shuffle(new_list)

    return new_list

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])

    # Set the seed
    my_seed = start_randomization(settings_dict['seed'])
    print(my_seed)
    # generate some values and print them out...
    for x in range(0, 9):
        print(get_random_int())
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle_list(my_list)
    print(my_list)