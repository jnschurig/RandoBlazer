# This is a weird compatibility thing.
# Allows the script to run from different contexts.
try: 
    from reference import constants, map
except:
    try: 
        import constants, map
    except: 
        pass

TEXT_END_MULTI = { # It's important to use actual byte arrays because ascii characters...
    "ENDTYPE_52FA": [b'\x13\x52\xFA'], 
    "ENDTYPE_88B9": [b'\x13\x88\xB9'],
    "ENDTYPE_46EC": [b'\x13\x46\xEC'],
    "ENDTYPE_1EA5": [b'\x13\x1E\xA5'],
    "ENDTYPE_A3BF": [b'\x13\xA3\xBF'],
    "ENDTYPE_DFF0": [b'\x13\xDF\xF0'],
    "ENDTYPE_44AA": [b'\x13\x44\xAA'], 
    "ENDTYPE_C5EE": [b'\x13\xC5\xEE']
}

TEXT_ENDING_12 = [b'\x12\x08\x08\x04\x0C']

TEXT_HERO_FOUND = [b'\x02\x02\xAF\x0D']

TEXT_HERO_RECEIVED = [b'\x02\x02\x20\xD4\x0D']

START_YELLOW_STYLE_TEXT = [b'\x03\x24']

END_YELLOW_STYLE_TEXT = [b'\x03\x20']

# Some npcs will restore health when they are released. Use this values prior to "delete" values
# Use with NPC_TO_DISABLE_ADDRESSES
HEAL_HERO = [b'\x37\x02']

# Will remove the "talking" box from releasing npcs
# Use with NPC_TO_DISABLE_ADDRESSES
DELETE_RELEASE_TEXT = [b'\x86\x6B']

GENERAL_TEXT = {
    "TITLE_TEXT": [
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
            'pad_value': ' ',
            'pad_dir': 'center'
        },
        {
            'address': 0x13B52,
            'value': 'SEED: ${seed}',
            'note': 'Second Line on the title screen',
            'length': 28,
            'pad_value': ' ',
            'pad_dir': 'center'
        },
        {
            'address': 0x13B70,
            'value': "QUINTET/ENIX 1992",
            'note': 'Third Line on the title screen',
            'length': 20,
            'pad_dir': 'right',
            'pad_value': ' '
        },
    ],
    "FILE_SELECT": [ 
        {
            'address': 0x143B9,
            'value': '${seed_hash}',
            'note': 'Shows up in the file select screen.',
            'length': 22
        }
    ],
    "MASTER_INTRO_TEXT": [
        {
            "address": 0x7999,
            "random_value": [
                "420 Soul blaze it!",
                "I`m calling\rSoul Blade in its\rvanilla location.",
                "Good luck!\rYou`ll need it!",
                "Are we on\rSpeedGaming yet?",
                "This run is\rZantetsu-less until\rZantetsu.",
                "It`s show time!",
                "Dancing grandmas\r    HYPE!!!!    ",
                "Thank you so much\rfor playing my game!",
                "Extra credit if\ryou get sub-2h!",
                "I`m calling pedestal\rseed on this one.",
                "Fun fact: there are\rexactly 400 monster\rlairs in this game.",
                "GLHF!",
                "Look mom,\rI`m on stream!!!",
                "Go and bring back\rthe peace!\r.....Or whatever this\rgame is about.",
                "This is totally\rnot a trolly seed.",
                "This seed is\rarmor-less until\rWorld of Evil.",
                "I can`t wait to\rsee the forced\rmagic-less Laynole.",
                "Break a leg!",
                "Initializing\rvideogame.....\r     .....complete!",
                "Super Nintendo is\rthe best console.\rFite me.",
                "So you think you\rhave what it takes?",
                "Let`s go!\rYou can do it!",
                "My PB on this\rseed is 35:37.\rBlindfolded.",
                "Help me,\rObi-Wan Kenobi.\rYou`re my only hope.",
                "Phoenix in hype cave.\rI`m calling it.",
                "Any resemblance with\rActRaiser is purely\rcoincidental."
            ],
            "value": ["${value}"] + TEXT_END_MULTI["ENDTYPE_52FA"]
        },
        {
            "address": 0x7A07,
            "value": TEXT_END_MULTI["ENDTYPE_52FA"]
        },
    ],
    "HERO_DEATH_MASTER_TEXT": [ 
        {
            "address": 0x786B,
            "random_value": [
                "Ouch! Tough luck :/",
                "Better luck next time!",
                "Don`t be patient.\rThis is a speedrun\rafter all.",
                "Cheer up!\rYou can do it!",
                "Trolly seed, huh?",
                "Git gud n00b\rLOL",
                "Don`t push yourself\rtoo hard.",
                "That death was\rRNG manipulation.",
                "I`m sorry for\rmaking this seed...",
                "Be more careful\rnext time!",
                "I`m sure this\rwas a deathwarp!\r       .....Right?",
                "Come on! Let`s go!",
                "Don`t give up.\rYou got this!"
            ],
            "value": ["${value}"] + TEXT_END_MULTI["ENDTYPE_52FA"]
        }
    ],
    "BROWNSTONE_GET_MASTER_TEXT": [ 
        {
            "address": 0x78BC,
            "value": ["One down,\rfive to go!"] + TEXT_END_MULTI["ENDTYPE_52FA"]
        }
    ],
    "DEATH_TOLL_INTRO_TEXT": [ 
        {
            "address": 0x4EF9,
            "random_value": [
                "Peekaboo!",
                "Guess who!",
                "Your adventure\rends here.",
                "Time for an\repic battle!",
                "In case you haven`t\rguessed, I`m the\rfinal boss.",
                "How did you make it\rhere? This seed was\rsupposed to be\rsuper trolly!",
                "Surpriiiiise!",
                "Incoming the game`s\rhardest fight.",
                "So we meet again,\rMr. Bond.",
                "I`ll put an end\rto your misery."
            ],
            "value": ["${value}"] + TEXT_ENDING_12
        }        
    ],
    "TRUE_DEATH_TOLL_INTRO_TEXT": [ 
        {
            "address": 0x4FB7,
            "random_value": [
                "This is not even\rmy final form!",
                "All right.\rNow this is\rserious business.",
                "I hope you didn`t\rforget Phoenix!",
                "Okay, time for an\ractually challenging\rbattle.",
                "Time to die!",
                "You didn`t think\rit was that easy,\rdid you?",
                "Loading Deathtoll.exe\r   .......Complete!",
                "Don`t tell me\ryou also got the\rSuper Bracelet!?",
                "And now behold...\rmy true power!",
                "Dang, I hope my next\rphase is better..."
            ],
            "value": ["${value}"] + TEXT_ENDING_12
        }
    ],
    "VICTORY_TEXT": [ 
        {
            "address": 0x5388,
            "value": ord(b'\x0B'),
            "note": "This changes the text address. Seems like there are two sets of text available."
        },
        {
            "address": 0x53C7,
            "value": TEXT_ENDING_12,
            "note": "Need to add certain endings. Probably to close text boxes."
        },
        {
            "address": 0x540C,
            "random_value": [
                "\r         G  G",
                "Thank you Mario.\rBut our princess\ris in another castle!",
                "Congratulations!",
                "Woohoo!!\rYou made it!!!",
                "Thanks a lot for\rplaying this\rrandomizer.",
                "Hope you enjoyed\rthis seed!",
                "A winner is you!",
                "Dang, I really\rthought this seed was\rtoo trolly for you.",
                "  ...and this is\rthe end of our story.",
                "The last Metroid\ris in captivity.\rThe galaxy is\rat peace.",
                "Well done!\rNow try Hard mode.\r\r   ...just kidding!",
                "I`m sorry for\rthis seed...",
                "Hi YouTube!",
                "This is the end.\rMy only friend,\rthe end.",
                "You are a true hero!",
                "Hyrule is saved!\r\r ...Wait, wrong game.",
                "That`s all folks!",
                "Well done!\rBut the next seed\rwon`t be that easy!"
        ],
        "value": ["${value}"] + TEXT_ENDING_12
        }
    ],
    "TYPO_FIXES": [ # Some basic fixes to text in the game.
        {
            "address": 0x150EC,
            "value": 're',
            "note": "Magic Flare text fix"
        },
        {
            "address": 0x1514C,
            "value": 'G.Leaf',
            "note": "Greenwood Leaves fix"
        },
        {
            "address": 0x151B2,
            "value": 'A.Leaf',
            "note": "Actinidia Leaves fix"
        },
        {
            "address": 0x1621E,
            "value": 'ei',
            "note": '"Received" fix'
        },
        {
            'address': 0x1591A,
            'value': 'spike floors',
            'note': 'Replace elemental mail text from "damage zones" to "spike floors"'
        },
    ],
    "BRIDGE_GUARD_TEXT": [
        {
            "address": 0x18644,
            "value": ['Please pass.'] + TEXT_END_MULTI["ENDTYPE_88B9"]
        }
    ],
    "WATER_MILL_KEEPER": [ 
        {
            "address": 0x1877C,
            "value": ['Could you please\rturn this wheel?'] + TEXT_END_MULTI["ENDTYPE_88B9"]
        },
        {
            "address": 0x188B9,
            "value": TEXT_END_MULTI["ENDTYPE_88B9"]
        }
    ],
    "LISA_DREAM_TEXT": [
        {
            "address": 0x1A522,
            "value": [ord(b'\x3C'), b'Lisa, you must\rhelp this one.', ord(b'\x3E')] # Closing quotation marks
                + TEXT_END_MULTI["ENDTYPE_88B9"]
        },
        {
            "address": 0x1A5AF,
            "value": TEXT_END_MULTI["ENDTYPE_88B9"]
        }
    ],
    "MAGICIAN_TEXT": [
        {
            "address": 0x1A914,
            "value": [b'Good luck and/or\rblame Everhate.'] + TEXT_END_MULTI["ENDTYPE_88B9"]
        }
    ]
}

FUNCTIONALITY_HACKS = {
    "OLD_WOMAN_PLACEMENT_HACK": [
        {
            "address": 0x18121,
            "value": b'\x3C\x20'
        }
    ],
    "LISA_HACK": [ 
        {
            "address": 0x18A6F,
            "value": ord(b'\x00'),
            "note": "Remove requirement to have certain item"
        },
        {
            "address": 0x18A7D,
            "value": b'\x7F\x8A',
            "note": "Change pointer when Village Chief is revived"
        }
    ],
    # Sleeping tulip (move this text to make room for the Pass tile text)
    "TULIP_TEXT": [
        {
            "address": 0x1984E,
            "value": ord(b'\x9A')
        },
        {
            "address": 0x1989A,
            "value": [ord(b'\x10'), 'Hello...']
        }
    ]
}

ITEM_PLACEMENT_HACKS = {
    "VILLAGE_CHIEF": [# We will change the key to be the same as the item location name
        {
            "address": 0x1A0C0,
            "value": ord(b'\x00'),
            "note": 'This should be an "impossible" item id.'
        },
        {
            "address": 0x1A123,
            "value": ord(b'\x33'),
            "note": 'Change pointer'
        },
        {
            "address": 0x1A125,
            "note": 'Content',
            "value": [b'\x02\x01\x91\xA1\x00\x5E'] # Text "Gives item"
                + [b'\x02\x0A', ord(b'\x00')] # Actually give the item # SECOND MEMBER IS RANDOMIZED ITEM ID.
                + [b'\x02\x09\x00\x9B\x6B'] # Set flag: item has been given
                + [b'\x02\x01\x72\xA2\x6B'] # Text when item is already given
        },
    ],
    "UNDERGROUND_CRYSTAL_FAIRY_1": [# This may need to be a general text hack.
        {
            "address": 0x1AC5B,
            "value": ord(b'\x00') # An item id I think...
        }
    ]
}

# Text when releasing certain NPCs.
NPC_TO_DISABLE_ADDRESSES = {
    "value": DELETE_RELEASE_TEXT, # End byte to replace text boxes.
    "addresses": [ 
        0x1815A, # Old Woman 
        0x184BA, # Tulip next to Village Chief's house 
        0x18775, # Water mill keeper 
        0x18BC4, # Lisa 
        0x19506, # Old man in Leo's Paintings house 
        # 0x1A13A, # Village Chief 
        0x1AA56, # Tulip next to Underground Castle 
        0x1CA7F, # Sleeping bird 
        # 0x1D532, # Greenwood's Guardian 
        0x1D869, # Mole (helping soul) 
        0x22E7F, # Great Door (helping soul) 
        0x22FF4, # Leo's cat 
        # 0x23559, # Marie 
        0x23FCA, # Soldier next to basement entrance 
        0x24616, # Singer 
        0x249D2, # Queen Magridd 
        0x2521B, # Soldier (helping soul) 
        # 0x255E5, # King Magridd 
        0x25BAF, # Soldier with Leo 
        0x25FE0, # Dr. Leo (when the two soldiers are not present) 
        0x26033, # Dr. Leo (when the two soldiers are present) 
        0xF8109, # Angelfish (helping soul) 
        0xF87FA, # Mermaid statue (Blester) 
        0xF8ACF, # Mermaid statue (Rockbird) 
        0xF8EEA, # Mermaid statue (Durean) 
        0xF966D, # Mermaid statue (Ghost Ship) 
        0xF9BF4  # Lue 
    ]
}

NPC_TO_HEAL_AND_DISABLE = {
    "value": HEAL_HERO + DELETE_RELEASE_TEXT,
    "addresses": [ 
        0x1A13A, # Village Chief 
        0x1D532, # Greenwood's Guardian 
        0x23559, # Marie 
        0x255E5, # King Magridd 
    ]
}
