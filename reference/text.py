# This is a weird compatibility thing.
# Allows the script to run from different contexts.
try: 
    from reference import constants
except:
    try: 
        import constants
    except: 
        pass

TITLE_TEXT = [
    {
        'address': 0x13B2B,
        'value': b'RANDO HYPE',
        'note': 'Replacement for "PUSH START". Must be no longer than 10 chars'
    },
    {
        'address': 0x13B3C,
        'value': 'RandoBlazer v' + constants.VERSION_CODE,
        'note': 'First Line on the title screen',
        'length': 19,
        'pad_value': ' '
    },
    {
        'address': 0x13B52,
        'value': 'COPYRIGHT 1992 QUINTET/ENIX',
        'note': 'Second Line on the title screen',
        'length': 26,
        'pad_value': ' ',
        'pad_dir': 'center'
    },
    {
        'address': 0x13B70,
        'value': "GET TO IT!",
        'note': 'Third Line on the title screen',
        'length': 20,
    },
    # {
    #     'address': 0x143B9,
    #     'value': b'SEED INFO567890',
    #     'note': ''
    # }
]

OTHER_TEXT = [
    {
        'address': 0x143B9,
        'value': 'SEED ${seed}',
        'note': 'Shows up in the file select screen.',
        'length': 22
    }
]

FILLER_REPLACEMENT = [
    {
        'address': 0x13B3C,
        'length': 19,
        'pad_value': ' ',
        'pad_dir': 'right'
    },
    {
        'address': 0x13B52,
        'length': 27,
        'pad_value': ' ',
        'pad_dir': 'right'
    },
    {
        'address': 0x13B70,
        'length': 20,
        'pad_value': ' '
    }
]
    