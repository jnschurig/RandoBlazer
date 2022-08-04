import os, sys, getopt
import hashlib, json
# import random_manager
from reference import constants

valid_args =  '''Valid Arguments: 
-h                  --help                         | Information about the script. 
-r <ROM Location>   --rom_path    <ROM Location>   | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc
-t <Target ROM>     --target_path <Target ROM>     | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc
-d                  --debug                        | Enable detailed output for debugging. 
'''

help_info  = '''Help Info:
This script will modify the contents ROM data and replace bits of it with other data.
The arguments are intended to be used for testing by running this script all by itself.
'''

def main(argv):
    arguments = {
        'rom_path': 'Soul Blazer (U) [!].smc',
        'target_path': 'output_rom.smc',
        'debug': False
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hr:t:d',['help','rom_path=','target_path=','debug'])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set Sthe arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-r', '--rom_path'):
            arguments['rom_path'] = arg
        elif opt in ('-t', '--target_path'):
            arguments['target_path'] = arg
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments

def check_hash(source_rom_path, debug=False):
    with open(source_rom_path, 'rb') as f:
        rom_data = f.read()
    
    rom_md5 = hashlib.md5(rom_data).hexdigest()

    if debug:
        print('DEBUG - Rom Hash: ' + rom_md5)

    payload = {
        'source_rom_path': source_rom_path,
        'rom_md5': rom_md5,
        'is_ok': False
    }

    if rom_md5 == constants.ROM_HASH_MD5_UNHEADERED:
        payload['is_ok'] = True
        payload['headered'] = False
        payload['rom_data'] = rom_data
    elif rom_md5 == constants.ROM_HASH_MD5_HEADERED:
        payload['is_ok'] = True
        payload['headered'] = True 
        payload['rom_data'] = rom_data[512:]

    return payload

# def initialize_file(source_rom_path, target_rom_path, file_has_header):
#     # Remove the target file if it exists.
#     try:
#         os.remove(target_rom_path)
#     except:
#         pass

#     with open(source_rom_path, 'rb') as f: 
#         with open(target_rom_path, 'wb') as g:
#             if file_has_header:
#                 print('Header Detected. Removing...')
#                 # This assumes a hex(200)/512 byte header.
#                 g.write(f.read()[512:])
#             else:
#                 g.write(f.read())

#     return True
    
def write_checks(rom_data, placement_dict):
    # Iterate through keys. Skip 'settings'...
    for key in placement_dict.keys():
        if key == 'settings':
            # Do nothing
            pass
        else:
            # Cycle through the list...
            for placement in placement_dict[key]:
                if placement['location']['type'] in ['chest']:
                    # 1. Set the location based on the location id...
                    address_offset = constants.CHEST_DATA_ADDRESS + (placement['location']['id'] * 3)

                    amount = 0
                    if placement['placement']['name'] == 'GEMS_EXP':
                        # Gem exp amount is handled in decimal as hex.
                        # We have to trick the system into thinking our 
                        # decimal amount is a hex amount, then convert 
                        # that back to decimal and set that. 
                        # ie, to get 40 gems in-game, we have to set 
                        # decimal amount 64.
                        amount = int(str(placement['placement']['amount']), 16)

                    try:
                        middle_part = placement['placement']['id'].to_bytes(1, 'little') + amount.to_bytes(2, 'little')
                        rom_data = modify_rom(rom_data, address_offset, middle_part)
                    except:
                        print('Failed to convert the byte data')
                        print('Placement:', json.dumps(placement))
                        sys.exit(2)
                else:
                    # We want to handle monster and lair and npc stuff eventually...
                    pass

    return rom_data

def replace_rom_text(rom_data, hack_name='ALL'):
    if hack_name != 'ALL':
        # find the one hack
        pass
    else:
        # Do them all
        pass

    return rom_data

def finalize_rom(rom_data, file_name):
    with open(file_name, 'wb') as f:
        f.write(rom_data)
    return file_name 

def modify_rom(rom_data, starting_edit_address, byte_array):
    end_edit_address = starting_edit_address + len(byte_array)

    return rom_data[:starting_edit_address] + byte_array + rom_data[end_edit_address:]

if __name__ == '__main__':
    # Get settings
    settings_dict = main(sys.argv[1:])

    # Use default paths...
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['rom_path'])
    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    # all_changes = compile_changes(settings_dict)
    rom_info = check_hash(source_rom_path, settings_dict['debug'])
    if settings_dict['debug']:
        print('DEBUG - ROM INFO')
        for key in rom_info.keys():
            if key != 'rom_data': # This sucker is too big to write out.
                print('DEBUG - ' + str(key) + ': ' + str(rom_info[key]))

    sample_placement = {
    "0": [
            {
                "location": {
                    "type": "chest",
                    "id": 0,
                    "name": "SWORD_OF_LIFE",
                    "pretty_name": "placeholder text"
                },
                "placement": {
                    "type": "item",
                    "name": "RECOVERY_SWORD",
                    "id": 7,
                    "pretty_name": "Recovery Sword"
                }
        }],
    "1": [
        {
            "location": {
                "type": "item",
                "name": "ITEM_CHEST_OF_DRAWERS_HERB",
                "id": 102,
                "pretty_name": "Medical Herb Drawers"
            },
            "placement": {
                "type": "item",
                "name": "GEMS_EXP",
                "amount": 600,
                "id": 255,
                "pretty_name": "Gems/EXP"
            }
            }
        ]
    }

    rom_data = write_checks(rom_info['rom_data'], sample_placement)

    file_path = finalize_rom(rom_data, target_rom_path)
    print(file_path)
