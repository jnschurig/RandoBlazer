from reference import lairs, map, items

# Using the contents of many of our reference data files,
# Create a list of elements from the game. 
# We will select a few items from the list randomly as part of randomization
# and possibly use that instead of the seed in the file select.
# This will be done as an option for race security and the like.

def generate_hash_members():

    all_things = []

    exceptions = ['ACT_MAX', 'NO_ENEMY', 'OF', 'NEAR', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'EMBLEM', 'GEMS_EXP', 'NOTHING', '_SWORD']

    replacement_text = [
        {'text': 'ACT1_'},
        {'text': 'ACT2_'},
        {'text': 'ACT3_'},
        {'text': 'ACT4_'},
        {'text': 'ACT5_'},
        {'text': 'ACT6_'},
        {'text': 'ACT7_'},
        {'text': 'ITEM_CRYSTAL_'},
        {'text': 'ITEM_'},
        {'text': '_NO_ENEMY'},
        {'text': '_', 'replacement_val': ' '},
    ]

    for key in lairs.LAIR_ACTS.keys():
        all_things.append(key)

    for key in map.LOCATION_ID_LOOKUP.keys():
        split_key = key.split('_')
        for key_part in split_key:
            all_things.append(key_part)

    for key in items.ITEMS.keys():
        all_things.append(key)

    good_things = []

    for thing in all_things:
        for replacement in replacement_text:
            if 'replacement_val' not in replacement:
                replacement['replacement_val'] = ''
            thing = thing.replace(replacement['text'], replacement['replacement_val'])
        if thing not in exceptions and thing not in good_things:
            good_things.append(thing)
    
    return good_things

if __name__ == '__main__':
    hash_list = generate_hash_members()
    print(hash_list)
    print('length:', len(hash_list))
