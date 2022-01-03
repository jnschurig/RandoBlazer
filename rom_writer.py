import os, sys, getopt
import binascii, shutil
from reference import constants, text

valid_args =  "-h                --help                       | Information about the script. \n"
valid_args += "-r <ROM Location> --rom_path    <ROM Location> | Path to the source ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/Soul Blazer (U) [!].smc \n"
valid_args += "-t <Target ROM>   --target_path <Target ROM>   | Path to target ROM. Can be fully qualified or relative to repository root. Defaults to ./REPOSITORY_ROOT_DIR/output_rom.smc \n"

help_info  = "Help Info: \n"
help_info += "This script will modify the contents ROM data and replace bits of it with other data. \n"
help_info += "The arguments are intended to be used for testing by running this script all by itself. \n"

def main(argv):
    arguments = {
        'rom_path': 'Soul Blazer (U) [!].smc',
        'target_path': 'output_rom.smc'
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hr:t:',['help','rom_path=','target_path='])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-r', '--rom_path'):
            arguments['rom_path'] = arg.lower()
        elif opt in ('-t', '--target_path'):
            arguments['target_path'] = arg.lower()
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments
    # End main

def modify_rom_data(target_rom_location, change_list):
    with open(target_rom_location, 'r+b') as f:
        for change in change_list:
            # change = json.loads(change)
            if 'value' not in change: # We might want to pad an existing item...
                    # change['value'] = ''
                    change_val = ''
            else:
                change_val = change['value']

            if 'length' in change: # We need to do some padding...
                change_val = change_val[:change['length']] # truncate to the length, if needed.
                if 'pad_value' not in change:
                    change['pad_value'] = ' '
                if 'pad_dir' not in change:
                    change['pad_dir'] = 'right'
                if change['pad_dir'] == 'right':
                    change_val = change_val.ljust(change['length'], change['pad_value'])
                if change['pad_dir'] == 'left':
                    change_val = change_val.rjust(change['length'], change['pad_value'])
                if change['pad_dir'] == 'center':
                    change_val = change_val.center(change['length'], change['pad_value'])

                if 'pad_right' not in change:
                    change['pad_right'] = True
                if change['pad_right']:
                    change_val = change_val.ljust(change['length'], change['pad_value'])
                else:
                    change_val = change_val.rjust(change['length'], change['pad_value'])

            if 'value' in change:
                if type(change_val) is str:
                    change_val = bytearray(change_val, 'utf-8')
                if type(change_val) is int:
                    change_val = bytearray(change_val)
            else:
                # change['value'] = 0x00
                # change['value'] = ''
                # change += ",'value': ''"
                pass


            # change['address'] = bytearray(hex(change['address']).upper(), 'utf-8')

            # print(type(change['address']))
            # print(change['address'])

            # print(type(change['value']))
            # print(change['value'])
            f.seek(change['address'])
            if type(change_val) is bytes: # if bytes
                f.write(change_val) # write directly
            elif type(change_val) is str: # if string
                f.write(binascii.hexlify(change_val)) # convert to bytes
            else: # This may be redundant, but it might be good to handle things that aren't strings a little differently.
                f.write(change_val)
        
        # for change in text.TITLE_TEXT:
        #     f.seek(change['address'])
        #     f.write(change['value'])
    
    return target_rom_location

def compile_changes():

    # change_list_file = os.path.join(constants.REPOSITORY_ROOT_DIR, 'change_list.json')

    change_list = []
    # change_list.append(text.FILLER_REPLACEMENT)
    # for item in text.FILLER_REPLACEMENT:
    #     change_list.append(item)
    for item in text.TITLE_TEXT:
        change_list.append(item)
    # change_list.append(text.TITLE_TEXT)
    
    return change_list


if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['rom_path'])
    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    all_changes = compile_changes()
    # print(change_list_file)

    # print(0x13B2B)

    try:
        os.remove(target_rom_path)
    except:
        pass

    shutil.copy(source_rom_path, target_rom_path)

    result_path = modify_rom_data(target_rom_path, all_changes)
    print(result_path)

    # with open(target_rom_path, 'wb') as f:
    #     f.write(rom_content)
