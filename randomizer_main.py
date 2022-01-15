import os, sys, getopt#, random
import rom_writer, random_manager, hash_maker
from reference import rom_data, text, qol, world, items, lairs, map, constants

valid_args =  "-h                  --help                         | Information about the script. \n"
valid_args += "-r <ROM Location>   --rom_path    <ROM Location>   | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc \n"
valid_args += "-t <Target ROM>     --target_path <Target ROM>     | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc \n"
valid_args += "-d                  --debug                        | Enable detailed output for debugging. Default is False. \n"
valid_args += "-z <Setting String> --randomize   <Setting String> | Apply Randomization with settings. \n"
valid_args += "-q <QOL String>     --qol         <QOL String>     | Quality of Life Settings. Text speed (Tnormal,Tfast,Tfaster,Tinstant) \n"
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

def get_text_changes(settings={}):
    text_changes = []

    for item in text.TITLE_TEXT:
        rom_edit = {}
        if type(item['value']) is str:
            # Check for variable replacements...
            if 'race' in settings:
                item['value'] = "Let the race begin!"
            elif 'seed' in settings:
                item['value'] = item['value'].replace('${seed}', settings['seed'])
            else:
                item['value'] = 'Good luck out there!'
        rom_edit['value'] = rom_writer.to_bytes(item)
        rom_edit['address'] = item['address']

        text_changes.append(rom_edit)

    for item in text.FILE_SELECT:
        rom_edit = {}
        if type(item['value']) is str:
            # Check for variable replacements
            if 'seed_hash' in settings:
                item['value'] = item['value'].replace('${seed_hash}', settings['seed_hash'])
            else:
                item['value'] = 'FILE SELECT'
        rom_edit['value'] = rom_writer.to_bytes(item)
        rom_edit['address'] = item['address']

        text_changes.append(rom_edit)

    return text_changes

def randomizer(settings):
    debug = settings['debug']
    # Check the ROM
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings['rom_path'])

    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    rom_info = rom_writer.check_hash(source_rom_path, settings['debug'])

    if debug: print(rom_info)

    if not rom_info['is_ok']:
        print('Input ROM not accepted.')
        if not debug: print('Use --debug for details')
        return False

    # Check settings
    seed = ''
    if settings['randomize']:
        # Start up the rng
        seed = random_manager.start_randomization(settings['seed'])
        settings['seed'] = seed
    if debug: print('Seed:', seed)

    # 
    if seed and seed != '':
        target_rom_path = target_rom_path.replace('.smc', '') + ' Randomizer - ' + str(seed) + '.smc'

    # Randomize Stuff

    # Get a seed hash
    hash_settings = {}
    for item in text.FILE_SELECT:
        if item['value'] == '${seed_hash}':
            hash_settings = item
            break 
    
    seed_hash = ''
    hash_members = hash_maker.generate_hash_members()
    while len(seed_hash) < (hash_settings['length'] - 2):
        idx = random_manager.get_random_int(0, len(hash_members)-1)
        member = hash_members[idx]
        if len(seed_hash) + len(member) < hash_settings['length']:
            seed_hash += member + ' '
    seed_hash = seed_hash.strip()
    settings['seed_hash'] = seed_hash
    if debug: print('Seed Hash:', seed_hash)

    # Initialize Rom
    rom_created = rom_writer.initialize_file(source_rom_path, target_rom_path, rom_info['headered'])
    if debug: 
        print('Output ROM created:', rom_created)
        print('Output ROM location:', target_rom_path)

    if rom_created:
        rom_writer.modify_rom_data(target_rom_path, get_text_changes(settings))

    # Do QOL Replacements


    # Generate a seed



    return True

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])

    rando_result = randomizer(settings_dict)
    print(rando_result)
