from reference import constants

TITLE_TEXT = [
    {
        'address': 0x13B2B,
        'value': b'RANDO HYPE',
        'note': 'Replacement for "PUSH START"'
    },
    {
        'address': 0x13B3C,
        'value': bytearray('RandoBlazer v' + constants.VERSION_CODE, 'utf-8'),
        'note': 'First Line on the title screen',
        'length': 20,
        'pad_value': ' '
    },
    {
        'address': 0x13B52,
        'value': b'Hello there.',
        'note': 'Second Line on the title screen'
    },
    # {
    #     'address': 0x13B6F,
    #     'value': b'COPYRIGHT 1992 QUINTET/ENIX',
    #     'note': 'Third Line on the title screen'
    # },
    {
        'address': 0x143B9,
        'value': b'SEED INFO567890',
        'note': ''
    }
]

OTHER_TEXT = [
    {
        'address': 0x143B9,
        'value': b'SEED INFO567890',
        'note': 'Not sure where this is supposed to show up yet.'
    }
]

FILLER_REPLACEMENT = [
    {
        'address': 0x13B3C,
        'length': 19,
        'pad_value': ' ',
        'pad_right': True
    },
    {
        'address': 0x13B52,
        'length': 27,
        'pad_value': ' ',
        'pad_right': True
    },
    {
        'address': 0x13B70,
        'length': 20,
        'pad_value': ' '
    }
]
    