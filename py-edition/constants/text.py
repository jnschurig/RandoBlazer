import os 

script_dir = os.path.dirname(__file__)
version_file = os.path.join(script_dir, '..', 'version.txt')

with open(version_file, 'r') as f:
    version_code = f.read()

TITLE_TEXT = [
    {
        "address": 0x13B2B,
        "value": b'RANDO HYPE',
        "note": "Replacement for 'PUSH START'"
    },
    {
        "address": 0x13B3C,
        "value": bytearray('RandoBlazer version v' + version_code, 'utf-8'),
        "note": "First Line on the title screen"
    },
    {
        "address": 0x13B52,
        "value": b"Randomizer version 0.6",
        "note": "Second Line on the title screen"
    },
    {
        "address": 0x13B6F,
        "value": b"COPYRIGHT 1992 QUINTET/ENIX",
        "note": "Third Line on the title screen"
    },
    {
        "address": 0x143B9,
        "value": b"SEED INFO567890",
        "note": ""
    }
]

OTHER_TEXT = [
    {
        "address": 0x143B9,
        "value": b"SEED INFO567890",
        "note": "Not sure where this is supposed to show up yet."
    }
]

FILLER_REPLACEMENT = [
    {
        "address": 0x13B3C,
        "length": 19,
        "character": " "
    },
    {
        "address": 0x13B52,
        "length": 27,
        "character": " "
    },
    {
        "address": 0x13B70,
        "length": 20,
        "character": " "
    }
]
    