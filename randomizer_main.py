import os, sys, getopt, json
import rom_writer, random_manager, hash_maker, update_rom, generate_map
from reference import qol, text_and_hacks, constants

valid_args = '''Valid Arguments:
-h                --help                       | Information about the script. 
-r <ROM Location> --rom_path    <ROM Location> | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc 
-t <Target ROM>   --target_path <Target ROM>   | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc 
-d                --debug                      | Enable detailed output for debugging. Default is False. 
-z <Setting JSON> --randomize   <Setting JSON> | Apply Randomization with settings in json format. Submitted string will be hashed as JSON.
-q <QOL String>   --qol         <QOL String>   | Quality of Life Settings. Use colon(:) separated list for QoL items. Text speed (Tnormal,Tfast,Tfaster,Tinstant) 
-s <Seed>         --seed        <Seed>         | The seed used to prime the random number generator. If one is not specified, one will be provided. 
'''

help_info = '''Help Info: 
This script will modify the contents ROM data and replace bits of it with other data. 
The arguments are intended to be used for testing by running this script all by itself. 
'''

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

# def get_text_changes(settings={}):
#     text_changes = []

#     for item in text.TITLE_TEXT:
#         rom_edit = {}
#         if type(item['value']) is str:
#             # Check for variable replacements...
#             if 'race' in settings:
#                 item['value'] = "Let the race begin!"
#             elif 'seed' in settings:
#                 item['value'] = item['value'].replace('${seed}', settings['seed'])
#             else:
#                 item['value'] = 'Good luck out there!'
#         rom_edit['value'] = rom_writer.to_bytes(item)
#         rom_edit['address'] = item['address']

#         text_changes.append(rom_edit)

#     for item in text.FILE_SELECT:
#         rom_edit = {}
#         if type(item['value']) is str:
#             # Check for variable replacements
#             if 'seed_hash' in settings:
#                 item['value'] = item['value'].replace('${seed_hash}', settings['seed_hash'])
#             else:
#                 item['value'] = 'FILE SELECT'
#         rom_edit['value'] = rom_writer.to_bytes(item)
#         rom_edit['address'] = item['address']

#         text_changes.append(rom_edit)

#     return text_changes

def get_qol_changes(qol_string):
    qol_changes = []
    qol_list = qol_string.split(':')
    for qol_item in qol_list:
        # Text Speeeeeeeeed
        if qol_item[:1] == 'T': 
            for text_setting in qol.TEXT_SCROLL:
                speed_change = {
                    'address': text_setting['address'],
                    'value': text_setting['speed'][qol_item[1:]]
                }
                qol_changes.append(speed_change)
        if qol_item[:1] == 'PLACEHOLDER':
            # At the time of this writing we only have on QoL setting.
            pass

    return qol_changes

def randomizer(settings):
    debug = settings['debug']
    # Check the ROM
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings['rom_path'])

    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    rom_info = rom_writer.check_hash(source_rom_path, debug)

    if debug: print(rom_info)

    if not rom_info['is_ok']:
        print('Input ROM not accepted.')
        if not debug: print('Use --debug for details')
        return False

    # Randomize Stuff
    randomize = False
    if 'randomize' in settings and settings['randomize']:
        randomize = True
        # Start up the rng
        seed = random_manager.start_randomization(settings['seed'])
        settings['seed'] = seed
        if debug: print('Seed:', seed)

        # Check settings
        if type(settings['randomize']) is bool:
            # Randomize is true, but no settings exist. Use defaults
            settings['randomize'] = constants.DEFAULT_RANDO_SETTINGS
        elif type(settings['randomize']) is str:
            if settings['randomize'] == 'True':
                # Randomize is true, but no settings exist. Use defaults
                settings['randomize'] = constants.DEFAULT_RANDO_SETTINGS
            else:
                # Means we need to parse the settings to json (hopefully)
                settings['randomize'] = json.loads(settings['randomize'])
        elif type(settings['randomize']) is dict:
            # Do nothing I guess...
            pass
        
        # Create a function that will make a pretty string...
        rando_settings_str = 'placeholder'
        target_rom_path = target_rom_path.replace('.smc', '') + ' Randomizer - ' + rando_settings_str + '-' + str(seed) + '.smc'

        world_graph = generate_map.initialize_world(settings['randomize'])
        item_placements = generate_map.randomize_items(world_graph, settings['randomize'])
        print(len(item_placements))
        '''
        This is where we put ALL the randomization stuff. Then at the very end we'll generate the 
        friendly hash for putting it in the file select screen.
        '''

    # Initialize Rom
    rom_created = rom_writer.initialize_file(source_rom_path, target_rom_path, rom_info['headered'])
    if debug: 
        print('Output ROM created:', rom_created)
        print('Output ROM location:', target_rom_path)



    # Get a seed hash
    hash_settings = {}
    for item in text_and_hacks.FILE_SELECT:
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



    if rom_created:
        # Do QOL Replacements
        if 'qol' in settings and settings['qol'] != '':
            rom_writer.modify_rom_data(target_rom_path, get_qol_changes(settings['qol']))
        # All Randomizations
        if randomize:
            # Text Replacement
            # rom_writer.modify_rom_data(target_rom_path, get_text_changes(settings))
            rom_writer.modify_rom_data(target_rom_path, update_rom.rom_rando_update(settings))



    return True

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    if settings_dict['debug']:
        print(json.dumps(settings_dict, indent = 4))

    rando_result = randomizer(settings_dict)
    print(rando_result)
