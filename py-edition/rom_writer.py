import os, sys, binascii, getopt
from constants import text

valid_args =  "-h --help                           | Information about the script. \n"
valid_args += "-a <a info> --alpha <a info>        | first argument info. \n"

help_info  = "Help Info: \n"
help_info += "A description that can help, generally. \n"

def main(argv):
    arguments = {
        'alpha': '',
        'beta': ''
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'ha:',['help''alpha='])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-a', '--alpha'):
            arguments['user'] = arg.lower()
    
    # if arguments['alpha'] == '':
    #     sys.exit('No alpha found. Use -a or --alpha')

    if False: # Thank you, I hate it.
        print(args)

    return arguments
    # End main

def modify_rom_data(rom_data, change_list):
    for change in change_list:

        pass

    return rom_data


if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])