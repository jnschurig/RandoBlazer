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
    with open(target_rom_location, 'rb') as f:
    # rom_content = f.read()
    
        for change in change_list:
            if 'length' in change: # We need to do some padding...
                if 'value' not in change: # We might want to pad an existing item...
                    change['value'] = ''
                    if 'pad_right' not in change:
                        change['pad_right'] = True
                    if change['pad_right']:
                        change['value'].ljust(change['length'], change['pad_value'])
                    else:
                        change['value'].rjust(change['length'], change['pad_value'])


            if 'value' in change:
                if type(change['value']) is str:
                    change['value'] = bytearray(change['value'], 'utf-8')
                if type(change['value']) is int:
                    change['value'] = bytearray(change['value'])
            else:
                change['value'] = 0x00

            # change['address'] = bytearray(hex(change['address']).upper(), 'utf-8')

            # print(type(change['address']))
            # print(change['address'])

            # print(type(change['value']))
            # print(change['value'])

            f.seek(change['address'])
            f.write(binascii.hexlify(change['value']))
    
    return target_rom_location

# def manage_file_access(target_rom_location):
#     with open(target_rom_location, 'rb') as f:
#         # rom_content = f.read()
#         f.seek()

#     return 'hi'


if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    source_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['rom_path'])
    target_rom_path = os.path.join(constants.REPOSITORY_ROOT_DIR, settings_dict['target_path'])

    try:
        os.remove(target_rom_path)
    except:
        pass

    shutil.copy(source_rom_path, target_rom_path)

    # with open(source_rom_path, 'rb') as f:
    #     with open(target_rom_path, 'wb') as g:
    #         g.write(f)

    # print(type(0xc0010))
    # print(type(text.FILLER_REPLACEMENT[1]['address']))

    
    # rom_content = modify_rom_data(rom_content, text.FILLER_REPLACEMENT)
    result_path = modify_rom_data(target_rom_path, text.TITLE_TEXT)
    print(result_path)

    # with open(target_rom_path, 'wb') as f:
    #     f.write(rom_content)
