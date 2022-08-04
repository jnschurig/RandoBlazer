# This is a weird compatibility thing.
# Allows the script to run from different contexts.
try: 
    from reference import constants, map
except:
    try: 
        import constants, map
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
]

FILE_SELECT = [
    {
        'address': 0x143B9,
        'value': '${seed_hash}',
        'note': 'Shows up in the file select screen.',
        'length': 22
    }
]

# MULTI_TYPE_PREFIX = b'\x13'

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

# TEXT_ENDING_12 = [
#     b'\x12',
#     b'\x08',
#     b'\x08',
#     b'\x04',
#     b'\x0C',
# ]

# TEXT_HERO_FOUND = [
#     b'\x02',
#     b'\x02',
#     b'\xAF',
#     b'\x0D',
# ]

# TEXT_HERO_RECEIVED = [ 
#     b'\x02',
#     b'\x02',
#     b'\x20',
#     b'\xD4',
#     b'\x0D',
# ]

# START_YELLOW_STYLE_TEXT = [ 
#     b'\x03',
#     b'\x24',
# ]

# END_YELLOW_STYLE_TEXT = [ 
#     b'\x03',
#     b'\x20',
# ]

# # Some npcs will restore health when they are released. Use this values prior to "delete" values
# # Use with NPC_TO_DISABLE_ADDRESSES
# HEAL_HERO = [ 
#     b'\x37',
#     b'\x02',
# ]

# # Will remove the "talking" box from releasing npcs
# # Use with NPC_TO_DISABLE_ADDRESSES
# DELETE_RELEASE_TEXT = [ 
#     b'\x86',
#     b'\x6B',
# ]

MASTER_INTRO_TEXT = [
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
    }
]

HERO_DEATH_MASTER_TEXT = {
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

BROWNSTONE_GET_MASTER_TEXT = {
    "address": 0x78BC,
    "value": ["One down,\rfive to go!"] + TEXT_END_MULTI["ENDTYPE_52FA"]
}

DEATH_TOLL_INTRO_TEXT = {
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

TRUE_DEATH_TOLL_INTRO_TEXT = {
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

VICTORY_TEXT = [
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
]

# Some basic fixes to text in the game.
TYPO_FIXES = [ 
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
]

# Moves the old woman to Lisa's house
OLD_WOMAN_PLACEMENT_HACK = {
    "address": 0x18121,
    "value": b'\x3C\x20'
}

# ~~NOT DONE~~
# Tool shop owner text condition
TOOL_SHOP_OWNER_TEXT = {
    "address": 0x1839B,
    "value": map.LOCATION_ID_LOOKUP['ITEM_TOOL_SHOP_OWNER']
}

# ~~NOT DONE~~
TOOL_SHOP_OWNER_SON_TEXT = [ 
    {
        "address": 0x1922E,
        "value": map.LOCATION_ID_LOOKUP['ITEM_TEDDY']
    },
    {
        "address": 0x19256,
        "value": ['Fancy ', b'\x97\x0D'] 
                 + START_YELLOW_STYLE_TEXT
                 + [map.LOCATION_ID_LOOKUP['ITEM_TEDDY']] 
                 + END_YELLOW_STYLE_TEXT
                 + ['\rfor a billion dollars?', ord(b'\x0C')]

    },
]

BRIDGE_GUARD_TEXT = {
    "address": 0x18644,
    "value": ['Please pass.'] + TEXT_END_MULTI["ENDTYPE_88B9"]
}

WATER_MILL_KEEPER = [ 
    {
        "address": 0x1877C,
        "value": ['Could you please\rturn this wheel?'] + TEXT_END_MULTI["ENDTYPE_88B9"]
    },
    {
        "address": 0x188B9,
        "value": TEXT_END_MULTI["ENDTYPE_88B9"]
    }
]

LISA_HACK = [ 
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
]

# Sleeping tulip (move this text to make room for the Pass tile text)
TULIP_TEXT = [
    {
        "address": 0x1984E,
        "value": ord(b'\x9A')
    },
    {
        "address": 0x1989A,
        "value": [ord(b'\x10'), 'Hello...']
    }
]

# Gourmet Goat Hint See TextUpdate.cpp line 889

VILLAGE_CHIEF = [
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
]

LISA_DREAM_TEXT = [
    {
        "address": 0x1A522,
        "value": [ord(b'\x3C'), b'Lisa, you must\rhelp this one.', ord(b'\x3E')] # Closing quotation marks
               + TEXT_END_MULTI["ENDTYPE_88B9"]
    },
    {
        "address": 0x1A5AF,
        "value": TEXT_END_MULTI["ENDTYPE_88B9"]
    }
]

MAGICIAN_TEXT = {
    "address": 0x1A914,
    "value": [b'Good luck and/or\rblame Everhate.'] + TEXT_END_MULTI["ENDTYPE_88B9"]
}

UNDERGROUND_CRYSTAL_FAIRY_1 = {
    "address": 0x1AC5B,
    "value": ord(b'\x00') # An item id I think...
}

UNDERGROUND_CRYSTAL_FAIRY_2 = {
    "address": 0x1AE14,
    "value": ["I`ve got nothing\rfor you.", b'\x11\x0C']
}

# Line 979 in TextUpdate.cpp

# Text when releasing certain NPCs.
NPC_TO_DISABLE_ADDRESSES = {
    "value": [b'\x86\x6B'], # End byte to replace text boxes.
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
    "value": HEAL_HERO + [b'\x86\x6B'],
    "addresses": [ 
        0x1A13A, # Village Chief 
        0x1D532, # Greenwood's Guardian 
        0x23559, # Marie 
        0x255E5, # King Magridd 
    ]
}

NPC_ITEM_TEXT_ADDRESSES = [ 
    0x183AE, # Tool shop owner 
    0x188FD, # Emblem A tile 
    0x18A2C, # Goat pen corner 
    0x192DA, # Tool shop owner's son Teddy 
    0x19870, # A Pass 
    0x199DD, # Tile at end of child's secret cave 
    0x1A192, # Village Chief 
    0x1A7FA, # Magician (start of the game) 
    0x1AB84, # Recovery Sword crystal 
    0x1ABBA, # Grass Valley secret room crystal 
    0x1ACBB, # Underground Castle 1st part crystal  # D3 AB
    0x1BE57, # Red-Hot Mirror bird  # 46 EC
    0x1C1D9, # Magic Bell crystal  # 46 EC
    0x1D292, # Woodstin Trio   # 46 EC
    0x1D53B, # Greenwood's Guardian  # 46 EC
    0x1D827, # Greenwood Leaves  # 46 EC
    0x1DC1A, # Shield Bracelet mole  # 46 EC
    0x1E0DE, # Psycho Sword squirrel  # 46 EC
    0x1E1EF, # Emblem C squirrel  # 46 EC
    0x1E49F, # Water Shrine Strange Bottle  # 46 EC
    0x1E572, # Light Arrow crystal  # 46 EC
    0x1E360, # Lost Marsh crystal  # 46 EC
    0x1E6C0, # Water Shrine crystal  # 46 EC
    0x1EBC3, # Fire Shrine crystal  # 46 EC
    0x209D5, # Mountain King  # 1E A5
    0x20DDD, # Mushroom Shoes boy  # 1E A5
    0x210CD, # Nome  # 1E A5
    0x21A7A, # Emblem E snail  # 1E A5
    0x21EB0, # Emblem F tile  # 1E A5
    0x2249B, # Mountain of Souls crystal  # 1E A5
    0x21100, # Lune crystal  # 1E A5
    0x22ADD, # Emblem G under chest of drawers  # A3 BF
    0x22A7C, # Chest of drawers (Mystic Armor)  # A3 BF
    0x22BE3, # Herb Plant in Leo's Lab  # A3 BF
    0x2306D, # Leo's Cat (door key)  # A3 BF
    0x231AE, # Actinidia plant  # A3 BF
    0x23404, # Chest of drawers (Herb)  # A3 BF
    0x235AD, # Marie  # A3 BF
    0x23922, # Spark Bomb mouse  # A3 BF
    0x23F34, # Leo's Lab Basement crystal  # A3 BF
    0x23BC0, # Model Town 1 crystal  # A3 BF
    0x23C00, # Power Plant crystal  # A3 BF
    0x24317, # Elemental Mail soldier  # DF F0
    0x24AB7, # Super Bracelet tile  # DF F0
    0x24A47, # Queen Magridd (VIP card)  # DF F0
    0x24C80, # Platinum Card soldier  # DF F0
    0x24EBA, # Maid (Herb)  # DF F0
    0x253C4, # Emblem H tile  # DF F0
    0x2563A, # Magridd King  # DF F0
    0x264C4, # Leo on the Airship deck (Mobile key)  # DF F0
    0x26A17, # Harp String tile  # DF F0
    0,       # North-eastern Mermaid (Herb)  # 44 AA
    0xF8BF8, # Bubble Armor Mermaid  # 44 AA
    0xF909A, # Magic Flair Mermaid  # 44 AA
    0xF9280, # Mermaid Queen  # 44 AA
    0xF9874, # Red-Hot Stick Mermaid  # 44 AA
    0xF9C13, # Lue  # 44 AA
    0xFA9C6, # Rockbird crystal  # 44 AA
    0xF9C40, # Seabed crystal near Blester  # 44 AA
    0xFA060  # Seabed crystal near Durean  # 44 AA
]

# I'm not sure what 0 means here
# I think it means to remove text completely
# Or maybe it means that the text is not to be adjusted.
# "You already have my item" text. Some things dont't get any.
NPC_ALREADY_HAVE_ITEM_ADDRESSES = [ 
    0x18429, # Tool shop owner 
    0,       # Emblem A tile 
    0,       # Goat pen corner 
    0x19320, # Tool shop owner's son Teddy 
    0,       # A Pass 
    0,       # Tile at end of child's secret cave 
    0,       # Village Chief 
    0,       # Magician (start of the game) 
    0,       # Recovery Sword crystal 
    0,       # Grass Valley secret room crystal 
    0,       # Underground Castle 1st part crystal 
    0x1BED3, # Red-Hot Mirror bird 
    0x1C225, # Magic Bell crystal 
    0,       # Woodstin Trio 
    0,       # Greenwood's Guardian 
    0,       # Greenwood Leaves 
    0x1DD73, # Shield Bracelet mole 
    0x1E11C, # Psycho Sword squirrel 
    0x1E22C, # Emblem C squirrel 
    0,       # Water Shrine Strange Bottle 
    0,       # Light Arrow crystal 
    0,       # Lost Marsh crystal 
    0,       # Water Shrine crystal 
    0,       # Fire Shrine crystal 
    0,       # Mountain King 
    0x20E73, # Mushroom Shoes boy 
    0,       # Nome 
    0x21AB9, # Emblem E snail 
    0,       # Emblem F tile 
    0,       # Mountain of Souls crystal 
    0,       # Lune crystal 
    0,       # Emblem G under chest of drawers 
    0x22AB9, # Chest of drawers (Mystic Armor) 
    0x22C22, # Herb Plant in Leo's Lab 
    0,       # Leo's Cat (door key) 
    0x23201, # Actinidia plant 
    0x2342F, # Chest of drawers (Herb) 
    0,       # Marie 
    0x23977, # Spark Bomb mouse 
    0,       # Leo's Lab Basement crystal 
    0,       # Model Town 1 crystal 
    0,       # Power Plant crystal 
    0,       # Elemental Mail soldier 
    0,       # Super Bracelet tile 
    0x24A77, # Queen Magridd (VIP card) 
    0,       # Platinum Card soldier 
    0x24F0F, # Maid (Herb) 
    0,       # Emblem H tile 
    0,       # Magridd King 
    0,       # Leo on the Airship deck (Mobile key) 
    0,       # Harp String tile 
    0xF836D, # North-eastern Mermaid (Herb) 
    0,       # Bubble Armor Mermaid 
    0xF90B6, # Magic Flair Mermaid 
    0,       # Mermaid Queen 
    0xF98C7, # Red-Hot Stick Mermaid 
    0xF9D87, # Lue 
    0,       # Rockbird crystal 
    0,       # Seabed crystal near Blester 
    0        # Seabed crystal near Durean 
]

# This is how we place items?
NPC_ITEM_ADDRESSES = [
    0x183AB, # Tool shop owner 
    0x1875E, # Emblem A tile 
    0x18960, # Goat pen corner 
    0x19253, # Tool shop owner's son Teddy 
    0x1983B, # A Pass 
    0x19914, # Tile in child's secret cave 
    0x1A12D, # Village Chief - address modified 
    0x1A7E4, # Magician (start of the game) 
    0x1AB78, # Recovery Sword crystal 
    0x1AC26, # Grass Valley secret room crystal 
    0x1AD15, # Underground Castle 1st part crystal 
    0x1BE54, # Red-Hot Mirror bird 
    0x1C116, # Magic Bell crystal 
    0x1D120, # Woodstin Trio 
    0x1D525, # Greenwood's Guardian 
    0x1D81E, # Greenwood Leaves 
    0x1DC17, # Shield Bracelet mole 
    0x1E039, # Psycho Sword squirrel 
    0x1E1E3, # Emblem C squirrel 
    0x1E496, # Water Shrine Strange Bottle 
    0x1E569, # Light Arrow crystal 
    0x1E4E3, # Lost Marsh crystal 
    0x1E537, # Water Shrine crystal 
    0x1E5B5, # Fire Shrine crystal 
    0x205A5, # Mountain King 
    0x20D63, # Mushroom Shoes boy 
    0x210C1, # Nome 
    0x21A6E, # Emblem E snail 
    0x21EA7, # Emblem F tile 
    0x21EF5, # Mountain of Souls crystal 
    0x21F49, # Lune crystal 
    0x22A40, # Emblem G under chest of drawers 
    0x22A5B, # Chest of drawers (Mystic Armor) 
    0x22BC1, # Herb Plant in Leo's Lab 
    0x22FB3, # Leo's Cat (door key) 
    0x231AB, # Actinidia plant 
    0x23311, # Chest of drawers (Herb) 
    0x2354D, # Marie 
    0x238F6, # Spark Bomb mouse 
    0x23DFA, # Leo's Lab Basement crystal 
    0x23E4E, # Model Town 1 crystal 
    0x23E7E, # Power Plant crystal 
    0x242A3, # Elemental Mail soldier 
    0x2499B, # Super Bracelet tile 
    0x249C2, # Queen Magridd (VIP card) 
    0x24C3B, # Platinum Card soldier - address modified 
    0x24E94, # Maid (Herb) 
    0x25345, # Emblem H tile 
    0x255D9, # Magridd King 
    0x25F51, # Leo on the Airship deck (Mobile key) 
    0x26A0E, # Harp String tile 
    0xF8315, # North-eastern Mermaid (Herb) 
    0xF8B9F, # Bubble Armor Mermaid 
    0xF9097, # Magic Flair Mermaid 
    0xF9223, # Mermaid Queen 
    0xF9871, # Red-Hot Stick Mermaid 
    0xF9BEB, # Lue 
    0xFA467, # Rockbird crystal 
    0xFA4BB, # Seabed crystal near Blester 
    0xFA4EB, # Seabed crystal near Durean 
]

