import os, sys, getopt
import random_manager

valid_args =  "-h                  --help                         | Information about the script. \n"
valid_args += "-r <ROM Location>   --rom_path    <ROM Location>   | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc \n"
valid_args += "-t <Target ROM>     --target_path <Target ROM>     | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc \n"
valid_args += "-d                  --debug                        | Enable detailed output for debugging. Default is False. \n"
valid_args += "-z <Setting String> --randomize   <Setting String> | Apply Randomization with settings. \n"
valid_args += "-q <QOL String>     --qol         <QOL String>     | Quality of Life Settings. Use colon(:) separated list for QoL items. Text speed (Tnormal,Tfast,Tfaster,Tinstant) \n"
valid_args += "-s <Seed>           --seed        <Seed>           | The seed used to prime the random number generator. If one is not specified, one will be provided. \n"

help_info  = "Help Info: \n"
help_info += "This script will modify the contents ROM data and replace bits of it with other data. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'rom_path': 'Soul Blazer (U) [!].smc',
        'target_path': 'Soul Blazer.smc',
        'randomize': False,
        'qol': '',
        'debug': False,
        'seed': None
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hr:t:z:q:ds:',['help','rom_path=','target_path=','randomize=','qol=','debug','seed='])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-r', '--rom_path'):
            arguments['rom_path'] = arg
        elif opt in ('-t', '--target_path'):
            arguments['target_path'] = arg
        elif opt in ('-z', '--randomize'):
            arguments['randomize'] = arg
        elif opt in ('-q', '--qol'):
            arguments['qol'] = arg
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
        elif opt in ('-s', '--seed'):
            arguments['seed'] = arg
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])

