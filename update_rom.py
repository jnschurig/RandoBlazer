import rom_writer, random_manager
from reference import constants, text_and_hacks

def rom_text_replacement(text_py_member):
    rom_edit_list = []
    # Rom edits look like this:
    # {'address': 0x000000, 'value':[value1, value2]}

    if type(text_py_member) is dict:
        text_py_member = [text_py_member]
    
    for entry in text_py_member:
        rom_edit = {
            'address': entry['address'],
            'value': []
        }
        if type(entry['value']) is not list:
            entry['value'] = [entry['value']]
        if 'random_value' in entry:
            value_replacement = random_manager.get_random_list_member(entry['random_value'])
            for value in entry['value']:
                if type(value) is str and '${value}' in value: 
                    value = value.replace('${value}', value_replacement)
                rom_edit['value'].append(rom_writer.to_bytes(value))
        else:
            rom_edit['value'] += rom_writer.to_bytes(entry['value'])
        rom_edit_list.append(rom_edit)
    return rom_edit_list

def rom_rando_update(settings={}):
    change_list = []

    for item in text_and_hacks.TITLE_TEXT:
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

        change_list.append(rom_edit)

    for item in text_and_hacks.FILE_SELECT:
        rom_edit = {}
        if type(item['value']) is str:
            # Check for variable replacements
            if 'seed_hash' in settings:
                item['value'] = item['value'].replace('${seed_hash}', settings['seed_hash'])
            else:
                item['value'] = 'FILE SELECT'
        rom_edit['value'] = rom_writer.to_bytes(item)
        rom_edit['address'] = item['address']

        change_list.append(rom_edit)
        
    change_list += rom_text_replacement(text_and_hacks.DEATH_TOLL_INTRO_TEXT)
    change_list += rom_text_replacement(text_and_hacks.TRUE_DEATH_TOLL_INTRO_TEXT)
    change_list += rom_text_replacement(text_and_hacks.VICTORY_TEXT)
    change_list += rom_text_replacement(text_and_hacks.MASTER_INTRO_TEXT)
    change_list += rom_text_replacement(text_and_hacks.HERO_DEATH_MASTER_TEXT)
    change_list += rom_text_replacement(text_and_hacks.BROWNSTONE_GET_MASTER_TEXT)
    change_list += rom_text_replacement(text_and_hacks.TYPO_FIXES)
    change_list += rom_text_replacement(text_and_hacks.OLD_WOMAN_PLACEMENT_HACK)
    change_list += rom_text_replacement(text_and_hacks.TOOL_SHOP_OWNER_TEXT)
    change_list += rom_text_replacement(text_and_hacks.TOOL_SHOP_OWNER_SON_TEXT)
    change_list += rom_text_replacement(text_and_hacks.BRIDGE_GUARD_TEXT)
    change_list += rom_text_replacement(text_and_hacks.WATER_MILL_KEEPER)
    change_list += rom_text_replacement(text_and_hacks.LISA_HACK)
    change_list += rom_text_replacement(text_and_hacks.TULIP_TEXT)
    # change_list += rom_text_replacement(text_and_hacks.VILLAGE_CHIEF)
    change_list += rom_text_replacement(text_and_hacks.LISA_DREAM_TEXT)
    change_list += rom_text_replacement(text_and_hacks.MAGICIAN_TEXT)
    change_list += rom_text_replacement(text_and_hacks.UNDERGROUND_CRYSTAL_FAIRY_1)
    change_list += rom_text_replacement(text_and_hacks.UNDERGROUND_CRYSTAL_FAIRY_2)

    # Make a function for this ^ It's way too repetetive and long not to have one.

    return change_list

if __name__ == '__main__':
    # Run this with creds built in.
    rom_changes = rom_rando_update()
    print('ROM Changes')
    print(rom_changes)