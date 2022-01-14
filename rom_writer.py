import os, sys, getopt
import hashlib
# import binascii
# import shutil
from reference import constants, text, qol

valid_args =  "-h                  --help                         | Information about the script. \n"
valid_args += "-r <ROM Location>   --rom_path    <ROM Location>   | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc \n"
valid_args += "-t <Target ROM>     --target_path <Target ROM>     | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc \n"
valid_args += "-d                  --debug                        | Enable detailed output for debugging. Default is False. \n"
valid_args += "-z <Setting String> --randomize   <Setting String> | Apply Randomization with settings. \n"
valid_args += "-q <QOL String>     --qol         <QOL String>     | Quality of Life Settings. Text speed (Tnormal,Tfast,Tfaster,Tinstant) \n"

help_info  = "Help Info: \n"
help_info += "This script will modify the contents ROM data and replace bits of it with other data. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'rom_path': 'Soul Blazer (U) [!].smc',
        'target_path': 'output_rom.smc',
        'randomize': False,
        'qol': '',
        'debug': False
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hr:t:z:q:d',['help','rom_path=','target_path=','randomize=','qol=','debug'])
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
        elif opt in ('-z', '--randomize'):
            arguments['randomize'] = arg
        elif opt in ('-q', '--qol'):
            arguments['qol'] = arg
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments
    # End main

def modify_rom_data(target_rom_location, change_list):
    with open(target_rom_location, 'r+b') as f:
        for change in change_list:
            if type(change) is not dict:
                # Not going to make this change because it isn't formatted right.
                pass
            else:
                # We really want the values to be a list, even if it's only one.
                if type(change['value']) is list:
                    value_list = change['value']
                else:
                    value_list = [change['value']]

                # Go to the address.
                f.seek(change['address'])
                # Iterate through values and write changes.
                for change_val in value_list:
                    # If I have been good about the data compiler function, data will be 'bytes' or 'bytes-like'
                    f.write(change_val)

            # change = json.loads(change)
            # if 'value' not in change: # We might want to pad an existing item...
            #         # change['value'] = ''
            #         values = ['']
            # elif type(change['value']) is not list:
            #     values = [change['value']]
            # else:
            #     values = change['value']

            # if 'length' in change: # We need to do some padding...
            #     for change_val in values:
            #         change_val = change_val[:change['length']] # truncate to the length, if needed.
            #         if 'pad_value' not in change:
            #             change['pad_value'] = ' '
            #         if 'pad_dir' not in change:
            #             change['pad_dir'] = 'right'
            #         if change['pad_dir'] == 'right':
            #             change_val = change_val.ljust(change['length'], change['pad_value'])
            #         if change['pad_dir'] == 'left':
            #             change_val = change_val.rjust(change['length'], change['pad_value'])
            #         if change['pad_dir'] == 'center':
            #             change_val = change_val.center(change['length'], change['pad_value'])

            #         # if 'pad_right' not in change:
            #         #     change['pad_right'] = True
            #         # if change['pad_right']:
            #         #     change_val = change_val.ljust(change['length'], change['pad_value'])
            #         # else:
            #         #     change_val = change_val.rjust(change['length'], change['pad_value'])
            
            # # # if 'value' in change:
            # # for change_val in values:
            #         if type(change_val) is str:
            #             change_val = bytearray(change_val, 'utf-8')
            #         if type(change_val) is int:
            #             change_val = bytearray(change_val)
            #         # else:
            #             # change['value'] = 0x00
            #             # change['value'] = ''
            #             # change += ",'value': ''"
            #             # pass


                # f.seek(change['address'])
                # for change_val in values:
                #     if type(change_val) is bytes: # if bytes
                #         f.write(change_val) # write directly
                #     elif type(change_val) is str: # if string
                #         f.write(binascii.hexlify(change_val)) # convert to bytes
                #     elif type(change_val) is int:
                #         number_of_bytes = 1
                #         f.write(change_val.to_bytes(number_of_bytes, 'big'))
                #     else: # This may be redundant, but it might be good to handle things that aren't strings a little differently.
                #         f.write(change_val)
        
    return target_rom_location

def to_bytes(data):
    # Check main data types and convert it to a byte-like object (hopefully)
    # Lists utilize recursion to convert every item in the list to byte-like objects.

    data_dict = {}
    if type(data) is dict:
        # We should search for the 'value' field and attempt to process it as data.
        if 'value' in data:
            data_dict = data 
            data = data['value']
        else:
            # The default, for when we don't know what is in a dict.
            data = 0x00
        
    
    if type(data) is list:
        # Use recursion to compile every item in the list.
        # The only case in which the function will return
        # something other than a bytes-like object.
        new_list = []
        for value in data:
            new_list.append(to_bytes(value))
        return new_list
    elif type(data) is int:
        # Detect the minimum number of bytes required
        # Unless the number of bytes is specified in the data_dict
        if 'length' in data_dict:
            # The length in bytes has already been provided.
            data = data.to_bytes(data_dict['length'], 'big')
        else:
            length = 1
            while True:
                # Cycle through exponents until 
                if data < (256 ** length):
                    break
                # Increment by two because rom uses two byte pairs at each address.
                length += 1
            data = data.to_bytes(length, 'big')
    elif type(data) is str:
        if 'length' in data_dict: # We need to do some padding...
            # for change_val in data_dict:
            data = data[:data_dict['length']] # truncate to the length, if needed.
            if 'pad_value' not in data_dict:
                data_dict['pad_value'] = ' '
            if 'pad_dir' not in data_dict:
                data_dict['pad_dir'] = 'right'
            if data_dict['pad_dir'] == 'right':
                data = data.ljust(data_dict['length'], data_dict['pad_value'])
            elif data_dict['pad_dir'] == 'left':
                data = data.rjust(data_dict['length'], data_dict['pad_value'])
            elif data_dict['pad_dir'] == 'center':
                data = data.center(data_dict['length'], data_dict['pad_value'])
        
        # Convert to bytes-like object
        data = bytearray(data, 'utf-8')
        # this ^ returns a bytearray, which I'm pretty sure is right for strings.
        # data = binascii.hexlify(data)
        # This ^ will convert the bytearray into bytes, which I think is wrong.

    return data

# def compile_changes(inclusion_settings):
#     # Need to have a way of selectively compiling changes... 
#     # Maybe this function is not the right things...
#     change_list = []

#     # Quality of Life
#     if inclusion_settings['qol'] != '':
#         qol_list = inclusion_settings['qol'].split(':')
#         for qol_item in qol_list:
#             # Text Speeeeeeeeed
#             if qol_item[:1] == 'T': 
#                 for text_setting in qol.TEXT_SCROLL:
#                     speed_change = {
#                         'address': text_setting['address'],
#                         'value': text_setting['speed'][qol_item[1:]]
#                     }
#                     change_list.append(speed_change)
        

#     # change_list_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'change_list.json')
#     if inclusion_settings['randomize']:

#         for item in text.TITLE_TEXT:
#             change_list.append(item)
    
#     # Manual Testing
    
#     return change_list

def check_hash(source_rom_path, debug=False):
    with open(source_rom_path, 'rb') as f:
        # rom_data = f.read()
        rom_md5 = hashlib.md5(f.read()).hexdigest()

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
    elif rom_md5 == constants.ROM_HASH_MD5_HEADERED:
        payload['is_ok'] = True
        payload['headered'] = True 

    return payload

def initialize_file(source_rom_path, target_rom_path, file_has_header):
    # Remove the target file if it exists.
    try:
        os.remove(target_rom_path)
    except:
        pass

    with open(source_rom_path, 'rb') as f: 
        with open(target_rom_path, 'wb') as g:
            if file_has_header:
                print('Header Detected. Removing...')
                # This assumes a hex(200)/512 byte header.
                g.write(f.read()[512:])
            else:
                g.write(f.read())

    return True

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['rom_path'])
    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    # all_changes = compile_changes(settings_dict)
    rom_info = check_hash(source_rom_path)
    if settings_dict['debug']:
        print('DEBUG - ROM INFO')
        for key in rom_info.keys():
            print('DEBUG - ' + str(key) + ': ' + str(rom_info[key]))

    # print(0x13B2B)
    initialize_file(source_rom_path, target_rom_path, rom_info['headered'])

    # result_path = modify_rom_data(target_rom_path, all_changes)
    # print(result_path)

    # with open(target_rom_path, 'wb') as f:
    #     f.write(rom_content)
