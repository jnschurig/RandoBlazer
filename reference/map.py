# NUMBER_OF_REGIONS = 79

# NUMBER_OF_GOALS = 78

FLAGS = {
    'can_cut_metal': ['ZANTETSU_SWORD', 'SOUL_BLADE'],
    'can_cut_spirit': ['SPIRIT_SWORD', 'SOUL_BLADE'],
    'has_magic': [
        'FLAME_BALL',
        'LIGHT_ARROW',
        'MAGIC_FLARE',
        'ROTATOR',
        'SPARK_BOMB',
        'FLAME_PILLAR',
        'TORNADO',
    ],
    'has_thunder': ['THUNDER_RING', 'ZANTETSU_SWORD', 'SOUL_BLADE'],
}

# Idea from Tranq:
# Swords are found by name, but their power all simultaneously scales 
# based on how many you have found so far. Choosing a sword is still 
# valuable for its effect.

OPTIONS_LOOKUP = {
    'swords': [
        'SWORD_OF_LIFE',
        'PSYCHO_SWORD',
        'CRITICAL_SWORD',
        'LUCKY_BLADE',
        'ZANTETSU_SWORD',
        'SPIRIT_SWORD',
        'RECOVERY_SWORD',
        'SOUL_BLADE',
    ],
    'armor': [
        "IRON_ARMOR",
        "ICE_ARMOR",
        "BUBBLE_ARMOR",
        "MAGIC_ARMOR",
        "MYSTIC_ARMOR",
        "LIGHT_ARMOR",
        "ELEMENTAL_MAIL",
        "SOUL_ARMOR",
    ],
    'emblems': [
        "EMBLEM_A",
        "EMBLEM_B",
        "EMBLEM_C",
        "EMBLEM_D",
        "EMBLEM_E",
        "EMBLEM_F",
        "EMBLEM_G",
        "EMBLEM_H",
    ],
    'stones': [
        "BROWN_STONE",
        "GREEN_STONE",
        "BLUE_STONE",
        "SILVER_STONE",
        "PURPLE_STONE",
        "BLACK_STONE",
    ],
    'red_hots': [
        "RED_HOT_MIRROR",
        "RED_HOT_BALL",
        "RED_HOT_STICK",
    ],
    'bracelets': [
        "SHIELD_BRACELET",
        "POWER_BRACELET",
        "SUPER_BRACELET",
    ],
}


ITEM_TO_FLAGS = {
    'ZANTETSU_SWORD': ['can_cut_metal', 'has_thunder'],
    'SOUL_BLADE': ['can_cut_metal', 'has_thunder', 'can_cut_spirit'],
    'SPIRIT_SWORD': ['can_cut_spirit'],
    'THUNDER_RING': ['has_thunder'],
    'FLAME_BALL': ['has_magic'],
    'LIGHT_ARROW': ['has_magic'],
    'MAGIC_FLARE': ['has_magic'],
    'ROTATOR': ['has_magic'],
    'SPARK_BOMB': ['has_magic'],
    'FLAME_PILLAR': ['has_magic'],
    'TORNADO': ['has_magic'],
}

ADDITIONAL_LOGIC_REQUIREMENTS = {
    "MERMAIDS_TEARS": {
        "name": "Require Mermaid's Tears",
        "description": "Logically require Mermaid's Tears for hot Durean checks.",
        "regions": [77],
        "requirements": [{"type": "item", "name": "MERMAIDS_TEARS"}]
    },
    "ICE_ARMOR": {
        "name": "Require Ice Armor",
        "description": "Logically require Ice Armor for Leo's Lab basement 2 and Power Plant checks after Light Armor chest.",
        "regions": [66, 32],
        "requirements": [{"type": "item", "name": "ICE_ARMOR"}]
    },
}

CHECK_TYPE_LOOKUP = {
    'npc_id': ['lair'],
    'item': ['chest', 'item'],
    'flag': ['chest', 'item']
}

LOCATION_ID_LOOKUP = {
    "CHEST_SWORD_OF_LIFE"               : {"id": 0  , "pretty_name": "Sword of Life Chest"},
    "CHEST_IRON_ARMOR"                  : {"id": 1  , "pretty_name": "Iron Armor Chest"},
    "CHEST_GV_CHEST_ROOM_GEMS"          : {"id": 2  , "pretty_name": "Grass Valley Chest Room Gems"},
    "CHEST_UC_12_GEMS"                  : {"id": 3  , "pretty_name": "Underground Castle 12 Gems Chest"},
    "CHEST_UC_EARLY_HERB"               : {"id": 4  , "pretty_name": "Underground Castle Early Herb Chest"},
    "CHEST_DREAM_ROD"                   : {"id": 5  , "pretty_name": "Dream Rod Chest"},
    "CHEST_LEOS_BRUSH"                  : {"id": 6  , "pretty_name": "Leo's Brush Chest"},
    "CHEST_PAINTING_HERB"               : {"id": 7  , "pretty_name": "Leo's Paintings Herb Chest"},
    "CHEST_TORNADO"                     : {"id": 8  , "pretty_name": "Tornado Chest"},
    "CHEST_ICE_ARMOR"                   : {"id": 9  , "pretty_name": "Ice Armor Chest"},
    "CHEST_MOLES_RIBBON"                : {"id": 10 , "pretty_name": "Mole's Ribbon Chest"},
    "CHEST_MARSHES_GEMS_1"              : {"id": 11 , "pretty_name": "Lost Marshes First Gems Chest (50)"}, # Likely in water/fire shrine
    "CHEST_MARSHES_GEMS_2"              : {"id": 12 , "pretty_name": "Lost Marshes Second Gems Chest (150)"}, # Likely in water/fire shrine
    "CHEST_MARSHES_HERB_1"              : {"id": 13 , "pretty_name": "Lost Marshes First Herb Chest"}, # Likely in water/fire shrine
    "CHEST_DELICIOUS_SEEDS"             : {"id": 14 , "pretty_name": "Delicious Seeds Chest"},
    "CHEST_MARSHES_GEMS_3"              : {"id": 15 , "pretty_name": "Lost Marshes Third Gems Chest (50)"}, # Likely in water/fire shrine
    "CHEST_MARSHES_HERB_2"              : {"id": 16 , "pretty_name": "Lost Marshes Second Herb Chest"}, # Likely in water/fire shrine
    "CHEST_MARSHES_NOTHING"             : {"id": 17 , "pretty_name": "Lost Marshes Nothing Chest"}, # Likely in water/fire shrine
    "CHEST_FIRE_SHRINE_BOTTLE"          : {"id": 18 , "pretty_name": "Fire Shrine Strange Bottle Chest"}, 
    "CHEST_MARSHES_GEMS_4"              : {"id": 19 , "pretty_name": "Lost Marshes Fourth Gems Chest (100)"},
    "CHEST_MARSHES_GEMS_5"              : {"id": 20 , "pretty_name": "Lost Marshes Fifth Gems Chest (60)"},
    "CHEST_FLAME_PILLAR"                : {"id": 21 , "pretty_name": "Flame Pillar Chest"},
    "CHEST_MERMAID_TEARS"               : {"id": 22 , "pretty_name": "Mermaid's Tears Chest"},
    "CHEST_BIG_PEARL"                   : {"id": 23 , "pretty_name": "Big Pearl Chest"},
    "CHEST_EMBLEM_D"                    : {"id": 24 , "pretty_name": "Emblem D Chest"},
    "CHEST_HYPE_CAVE_GEMS"              : {"id": 25 , "pretty_name": "Hype Cave 80 Gems Chest"},
    "CHEST_HYPE_CAVE_HERB"              : {"id": 26 , "pretty_name": "Hype Cave Herb Chest"},
    "CHEST_HYPE_CAVE_NOTHING"           : {"id": 27 , "pretty_name": "Hype Cave Nothing Chest"},
    "CHEST_SOUTHERTA_HERB"              : {"id": 28 , "pretty_name": "Southerta Herb Chest"},
    "CHEST_ROCKBIRD_HERB"               : {"id": 29 , "pretty_name": "Rockbird Herb Chest"},
    "CHEST_ROCKBIRD_GEMS"               : {"id": 30 , "pretty_name": "Rockbird 60 Gems Chest"},
    "CHEST_CRITICAL_SWORD"              : {"id": 31 , "pretty_name": "Critical Sword Chest"},
    "CHEST_DUREAN_BOTTLE"               : {"id": 32 , "pretty_name": "Durean Strange Bottle Chest"},
    "CHEST_GHOST_SHIP_GEMS"             : {"id": 33 , "pretty_name": "Ghost Ship 1 Gem Chest"},
    "CHEST_POWER_BRACELET"              : {"id": 34 , "pretty_name": "Power Bracelet Chest"},
    "CHEST_MOUNTAIN_OF_SOULS_GEMS_1"    : {"id": 35 , "pretty_name": "Mountain of Souls 40 Gems Chest"},
    "CHEST_MAGIC_ARMOR"                 : {"id": 36 , "pretty_name": "Magic Armor Chest"},
    "CHEST_MOUNTAIN_OF_SOULS_NOTHING"   : {"id": 37 , "pretty_name": "Mountain of Souls Nothing Chest"},
    "CHEST_MOUNTAIN_OF_SOULS_HERB"      : {"id": 38 , "pretty_name": "Mountain of Souls Herb Chest"},
    "CHEST_MOUNTAIN_OF_SOULS_GEMS_2"    : {"id": 39 , "pretty_name": "Mountain of Souls 50 Gems Chest"},
    "CHEST_LUCKY_BLADE"                 : {"id": 40 , "pretty_name": "Lucky Blade Chest"},
    "CHEST_LUNE_BOTTLE"                 : {"id": 41 , "pretty_name": "Lune Strange Bottle Chest"},
    "CHEST_ROTATOR"                     : {"id": 42 , "pretty_name": "Rotator Chest"},
    "CHEST_ZANTETSU_SWORD"              : {"id": 43 , "pretty_name": "Zantetsu Sword Chest"},
    "CHEST_LIGHT_ARMOR"                 : {"id": 44 , "pretty_name": "Light Armor Chest"},
    "CHEST_MODEL_TOWN_1_GEMS_1"         : {"id": 45 , "pretty_name": "Model Town 1 50 Gems Chest"},
    "CHEST_MODEL_TOWN_1_HERB"           : {"id": 46 , "pretty_name": "Model Town 1 Herb Chest"},
    "CHEST_MODEL_TOWN_1_GEMS_2"         : {"id": 47 , "pretty_name": "Model Town 1 80 Gems Chest"},
    "CHEST_MODEL_TOWN_2_BOTTLE"         : {"id": 48 , "pretty_name": "Model Town 2 Strange Bottle Chest"},
    "CHEST_MODEL_TOWN_2_HERB"           : {"id": 49 , "pretty_name": "Model Town 2 Herb Chest"},
    "CHEST_MAGRIDD_BASEMENT_GEMS_1"     : {"id": 50 , "pretty_name": "Magridd Basement 80 Gems Chest"},
    "CHEST_SPIRIT_SWORD"                : {"id": 51 , "pretty_name": "Spirit Sword Chest"},
    "CHEST_MAGRIDD_BASEMENT_BOTTLE"     : {"id": 52 , "pretty_name": "Magridd Basement Strange Bottle Chest"},
    "CHEST_MAGRIDD_BASEMENT_HERB"       : {"id": 53 , "pretty_name": "Magridd Basement Herb Chest"},
    "CHEST_MAGRIDD_BASEMENT_GEMS_2"     : {"id": 54 , "pretty_name": "Magridd Basement 100 Gems Chest"},
    "CHEST_EMBLEM_B"                    : {"id": 55 , "pretty_name": "Emblem B Chest"},
    "CHEST_MAGRIDD_R_TOWER_GEMS_1"      : {"id": 56 , "pretty_name": "Magridd Right Tower First 80 Gems Chest"},
    "CHEST_MAGRIDD_R_TOWER_GEMS_2"      : {"id": 57 , "pretty_name": "Magridd Right Tower Second 80 Gems Chest"},
    "CHEST_MAGRIDD_R_TOWER_GEMS_3"      : {"id": 58 , "pretty_name": "Magridd Right Tower 100 Gems Chest"},
    "CHEST_MAGRIDD_R_TOWER_HERB"        : {"id": 59 , "pretty_name": "Magridd Right Tower Herb Chest"},
    "CHEST_WORLD_OF_EVIL_HERB"          : {"id": 60 , "pretty_name": "World of Evil Herb Chest"},
    "CHEST_WORLD_OF_EVIL_GEMS"          : {"id": 61 , "pretty_name": "World of Evil 200 Gems Chest"},
    "CHEST_RED_HOT_BALL"                : {"id": 62 , "pretty_name": "Red Hot Ball Chest"},
    "CHEST_SOUL_ARMOR"                  : {"id": 63 , "pretty_name": "Soul Armor Chest"},
    "CHEST_SOUL_BLADE"                  : {"id": 64 , "pretty_name": "Soul Blade Chest"},
    "CHEST_DAZZLING_SPACE_GEMS"         : {"id": 65 , "pretty_name": "Dazzling Space 100 Gems Chest"},
    "ITEM_TOOL_SHOP_OWNER"              : {"id": 66 , "pretty_name": "Tool Shop Owner"},
    "ITEM_EMBLEM_A"                     : {"id": 67 , "pretty_name": "Emblem A Tile"},
    "ITEM_GOAT_PEN"                     : {"id": 68 , "pretty_name": "Goat Pen Tile"},
    "ITEM_TEDDY"                        : {"id": 69 , "pretty_name": "Teddy"},
    "ITEM_PASS"                         : {"id": 70 , "pretty_name": "Pass Tile"},
    "ITEM_SECRET_CAVE_TILE"             : {"id": 71 , "pretty_name": "Secret Cave Tile"},
    "ITEM_VILLAGE_CHIEF"                : {"id": 72 , "pretty_name": "Village Chief"},
    "ITEM_MAGICIAN"                     : {"id": 73 , "pretty_name": "Magician Item"},
    "ITEM_CRYSTAL_RECOVERY_SWORD"       : {"id": 74 , "pretty_name": "Recovery Sword Crystal"},
    "ITEM_CRYSTAL_GRASS_VALLEY"         : {"id": 75 , "pretty_name": "Grass Valley Crystal"},
    "ITEM_CRYSTAL_UNDERGROUND_CASTLE"   : {"id": 76 , "pretty_name": "Underground Castle Crystal"},
    "ITEM_BIRD_RED_HOT_MIRROR"          : {"id": 77 , "pretty_name": "Red Hot Mirror Bird"},
    "ITEM_CRYSTAL_MAGIC_BELL"           : {"id": 78 , "pretty_name": "Magic Bell Crystal"},
    "ITEM_WOODSTIN_TRIO"                : {"id": 79 , "pretty_name": "Woodstin Trio"},
    "ITEM_GREENWOODS_GUARDIAN"          : {"id": 80 , "pretty_name": "Greenwood Guardian"},
    "ITEM_GREENWOOD_LEAVES"             : {"id": 81 , "pretty_name": "Greenwood Leaves Tile"},
    "ITEM_MOLE_SHIELD_BRACELET"         : {"id": 82 , "pretty_name": "Shield Bracelet Mole"},
    "ITEM_SQUIRREL_PSYCHO_SWORD"        : {"id": 83 , "pretty_name": "Psycho Sword Squirrel"},
    "ITEM_SQUIRREL_EMBLEM_C"            : {"id": 84 , "pretty_name": "Emblem C Squirrel"},
    "ITEM_WATER_SHRINE_TILE"            : {"id": 85 , "pretty_name": "Water Shrine Tile"},
    "ITEM_CRYSTAL_LIGHT_ARROW"          : {"id": 86 , "pretty_name": "Light Arrow Crystal"},
    "ITEM_CRYSTAL_LOST_MARSH"           : {"id": 87 , "pretty_name": "Lost Marsh Crystal"},
    "ITEM_CRYSTAL_WATER_SHRINE"         : {"id": 88 , "pretty_name": "Water Shrine Crystal"},
    "ITEM_CRYSTAL_FIRE_SHRINE"          : {"id": 89 , "pretty_name": "Fire Shrine Crystal"},
    "ITEM_MOUNTAIN_KING"                : {"id": 90 , "pretty_name": "Mountain King"},
    "ITEM_BOY_MUSHROOM_SHOES"           : {"id": 91 , "pretty_name": "Mushroom Shoes Boy"},
    "ITEM_NOME"                         : {"id": 92 , "pretty_name": "Nome"},
    "ITEM_SNAIL_EMBLEM_E"               : {"id": 93 , "pretty_name": "Emblem E Snail"},
    "ITEM_EMBLEM_F"                     : {"id": 94 , "pretty_name": "Emblem F Tile"},
    "ITEM_CRYSTAL_MOUNTAIN_OF_SOULS"    : {"id": 95 , "pretty_name": "Mountain of Souls Crystal"},
    "ITEM_CRYSTAL_LUNE"                 : {"id": 96 , "pretty_name": "Lune Crystal"},
    "ITEM_EMBLEM_G"                     : {"id": 97 , "pretty_name": "Emblem G Tile (Push Drawers)"},
    "ITEM_CHEST_OF_DRAWERS_MYSTIC_ARMOR": {"id": 98 , "pretty_name": "Mystic Armor Drawers"},
    "ITEM_PLANT_HERB"                   : {"id": 99 , "pretty_name": "Medical Herb Plant"},
    "ITEM_CAT_DOOR_KEY"                 : {"id": 100, "pretty_name": "Door Key Cat"},
    "ITEM_PLANT_ACTINIDIA_LEAVES"       : {"id": 101, "pretty_name": "Actinidia Plant"},
    "ITEM_CHEST_OF_DRAWERS_HERB"        : {"id": 102, "pretty_name": "Medical Herb Drawers"},
    "ITEM_MARIE"                        : {"id": 103, "pretty_name": "Marie"},
    "ITEM_MOUSE_SPARK_BOMB"             : {"id": 104, "pretty_name": "Spark Bomb Mouse"},
    "ITEM_CRYSTAL_LEOS_LAB_BASEMENT"    : {"id": 105, "pretty_name": "Lab Basement Crystal"},
    "ITEM_CRYSTAL_MODEL_TOWN"           : {"id": 106, "pretty_name": "Model Town Crystal"},
    "ITEM_CRYSTAL_POWER_PLANT"          : {"id": 107, "pretty_name": "Power Plant Crystal"},
    "ITEM_SOLDIER_ELEMENTAL_MAIL"       : {"id": 108, "pretty_name": "Elemental Mail Soldier"},
    "ITEM_SUPER_BRACELET"               : {"id": 109, "pretty_name": "Super Bracelet Tile"},
    "ITEM_QUEEN_MAGRIDD"                : {"id": 110, "pretty_name": "Queen Magridd"},
    "ITEM_SOLDIER_PLATINUM_CARD"        : {"id": 111, "pretty_name": "Platinum Card Soldier Tile"},
    "ITEM_MAID_HERB"                    : {"id": 112, "pretty_name": "Medical Herb Maid"},
    "ITEM_EMBLEM_H"                     : {"id": 113, "pretty_name": "Emblem H Tile (Castle Magridd)"},
    "ITEM_KING_MAGRIDD"                 : {"id": 114, "pretty_name": "King Magridd"},
    "ITEM_DR_LEO"                       : {"id": 115, "pretty_name": "Dr Leo"},
    "ITEM_HARP_STRING"                  : {"id": 116, "pretty_name": "Harp String Tile"},
    "ITEM_MERMAID_HERB"                 : {"id": 117, "pretty_name": "Medical Herb Mermaid"},
    "ITEM_MERMAID_BUBBLE_ARMOR"         : {"id": 118, "pretty_name": "Bubble Armor Mermaid"},
    "ITEM_MERMAID_MAGIC_FLARE"          : {"id": 119, "pretty_name": "Magic Flare Mermaid"},
    "ITEM_MERMAID_QUEEN"                : {"id": 120, "pretty_name": "Mermaid Queen"},
    "ITEM_MERMAID_RED_HOT_STICK"        : {"id": 121, "pretty_name": "Red Hot Stick Mermaid"},
    "ITEM_LUE"                          : {"id": 122, "pretty_name": "Lue"},
    "ITEM_CRYSTAL_ROCKBIRD"             : {"id": 123, "pretty_name": "Rockbird Crystal"},
    "ITEM_CRYSTAL_SEABED_NEAR_BLESTER"  : {"id": 124, "pretty_name": "Seabed Near Blester Crystal"},
    "ITEM_CRYSTAL_SEABED_NEAR_DUREAN"   : {"id": 125, "pretty_name": "Seabed Near Durean Crystal"},
}

NPC_ID = {
    "NPC_OLD_WOMAN"                     : {"id": 2  , "pretty_name": "placeholder"},
    "NPC_TOOL_SHOP_OWNER"               : {"id": 6  , "pretty_name": "placeholder"},
    "NPC_TULIP"                         : {"id": 7  , "pretty_name": "placeholder"},
    "NPC_BRIDGE_GUARD"                  : {"id": 8  , "pretty_name": "placeholder"},
    "NPC_VILLAGE_CHIEF"                 : {"id": 9  , "pretty_name": "placeholder"},
    "NPC_IVY_CHEST_ROOM"                : {"id": 13 , "pretty_name": "placeholder"},
    "NPC_WATER_MILL"                    : {"id": 14 , "pretty_name": "placeholder"},
    "NPC_GOAT_HERB"                     : {"id": 15 , "pretty_name": "placeholder"},
    "NPC_LISA"                          : {"id": 16 , "pretty_name": "placeholder"},
    "NPC_TULIP2"                        : {"id": 17 , "pretty_name": "placeholder"},
    "NPC_ARCHITECT"                     : {"id": 18 , "pretty_name": "placeholder"},
    "NPC_IVY"                           : {"id": 19 , "pretty_name": "placeholder"},
    "NPC_GOAT"                          : {"id": 21 , "pretty_name": "placeholder"},
    "NPC_TEDDY"                         : {"id": 22 , "pretty_name": "placeholder"},
    "NPC_TULIP3"                        : {"id": 24 , "pretty_name": "placeholder"},
    "NPC_LEOS_HOUSE"                    : {"id": 26 , "pretty_name": "placeholder"},
    "NPC_LONELY_GOAT"                   : {"id": 29 , "pretty_name": "placeholder"},
    "NPC_TULIP_PASS"                    : {"id": 34 , "pretty_name": "placeholder"},
    "NPC_BOY_CABIN"                     : {"id": 35 , "pretty_name": "placeholder"},
    "NPC_BOY_CAVE"                      : {"id": 37 , "pretty_name": "placeholder"},
    "NPC_OLD_MAN"                       : {"id": 40 , "pretty_name": "placeholder"},
    "NPC_OLD_MAN2"                      : {"id": 41 , "pretty_name": "placeholder"},
    "NPC_IVY2"                          : {"id": 42 , "pretty_name": "placeholder"},
    "NPC_IVY_EMBLEM_A"                  : {"id": 43 , "pretty_name": "placeholder"},
    "NPC_IVY_RECOVERY_SWORD"            : {"id": 44 , "pretty_name": "placeholder"},
    "NPC_TULIP4"                        : {"id": 46 , "pretty_name": "placeholder"},
    "NPC_GOAT2"                         : {"id": 47 , "pretty_name": "placeholder"},
    "NPC_BIRD_RED_HOT_MIRROR"           : {"id": 55 , "pretty_name": "placeholder"},
    "NPC_BIRD"                          : {"id": 56 , "pretty_name": "placeholder"},
    "NPC_DOG"                           : {"id": 60 , "pretty_name": "placeholder"},
    "NPC_DOG2"                          : {"id": 61 , "pretty_name": "placeholder"},
    "NPC_DOG3"                          : {"id": 63 , "pretty_name": "placeholder"},
    "NPC_MOLE_SHIELD_BRACELET"          : {"id": 64 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL_EMBLEM_C"             : {"id": 65 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL_PSYCHO_SWORD"         : {"id": 67 , "pretty_name": "placeholder"},
    "NPC_BIRD2"                         : {"id": 70 , "pretty_name": "placeholder"},
    "NPC_MOLE_SOUL_OF_LIGHT"            : {"id": 73 , "pretty_name": "placeholder"},
    "NPC_DEER"                          : {"id": 74 , "pretty_name": "placeholder"},
    "NPC_CROCODILE"                     : {"id": 78 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL"                      : {"id": 79 , "pretty_name": "placeholder"},
    "NPC_GREENWOODS_GUARDIAN"           : {"id": 80 , "pretty_name": "placeholder"},
    "NPC_MOLE"                          : {"id": 81 , "pretty_name": "placeholder"},
    "NPC_DOG4"                          : {"id": 86 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL_ICE_ARMOR"            : {"id": 88 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL2"                     : {"id": 89 , "pretty_name": "placeholder"},
    "NPC_DOG5"                          : {"id": 90 , "pretty_name": "placeholder"},
    "NPC_CROCODILE2"                    : {"id": 91 , "pretty_name": "placeholder"},
    "NPC_MOLE2"                         : {"id": 92 , "pretty_name": "placeholder"},
    "NPC_SQUIRREL3"                     : {"id": 93 , "pretty_name": "placeholder"},
    "NPC_BIRD_GREENWOOD_LEAF"           : {"id": 97 , "pretty_name": "placeholder"},
    "NPC_MOLE3"                         : {"id": 98 , "pretty_name": "placeholder"},
    "NPC_DEER_MAGIC_BELL"               : {"id": 99 , "pretty_name": "placeholder"},
    "NPC_BIRD3"                         : {"id": 100, "pretty_name": "placeholder"},
    "NPC_CROCODILE3"                    : {"id": 111, "pretty_name": "placeholder"},
    "NPC_MONMO"                         : {"id": 114, "pretty_name": "placeholder"},
    "NPC_DOLPHIN"                       : {"id": 124, "pretty_name": "placeholder"},
    "NPC_ANGELFISH"                     : {"id": 131, "pretty_name": "placeholder"},
    "NPC_MERMAID"                       : {"id": 132, "pretty_name": "placeholder"},
    "NPC_ANGELFISH2"                    : {"id": 134, "pretty_name": "placeholder"},
    "NPC_MERMAID_PEARL"                 : {"id": 138, "pretty_name": "placeholder"},
    "NPC_MERMAID2"                      : {"id": 139, "pretty_name": "placeholder"},
    "NPC_DOLPHIN_SAVES_LUE"             : {"id": 140, "pretty_name": "placeholder"},
    "NPC_MERMAID_STATUE_BLESTER"        : {"id": 141, "pretty_name": "placeholder"},
    "NPC_MERMAID_RED_HOT_STICK"         : {"id": 142, "pretty_name": "placeholder"},
    "NPC_LUE"                           : {"id": 143, "pretty_name": "placeholder"},
    "NPC_MERMAID3"                      : {"id": 146, "pretty_name": "placeholder"},
    "NPC_MERMAID_NANA"                  : {"id": 149, "pretty_name": "placeholder"},
    "NPC_MERMAID4"                      : {"id": 153, "pretty_name": "placeholder"},
    "NPC_DOLPHIN2"                      : {"id": 155, "pretty_name": "placeholder"},
    "NPC_MERMAID_STATUE_ROCKBIRD"       : {"id": 157, "pretty_name": "placeholder"},
    "NPC_MERMAID_BUBBLE_ARMOR"          : {"id": 161, "pretty_name": "placeholder"},
    "NPC_MERMAID5"                      : {"id": 164, "pretty_name": "placeholder"},
    "NPC_MERMAID6"                      : {"id": 165, "pretty_name": "placeholder"},
    "NPC_MERMAID_TEARS"                 : {"id": 167, "pretty_name": "placeholder"},
    "NPC_MERMAID_STATUE_DUREAN"         : {"id": 171, "pretty_name": "placeholder"},
    "NPC_ANGELFISH3"                    : {"id": 173, "pretty_name": "placeholder"},
    "NPC_ANGELFISH_SOUL_OF_SHIELD"      : {"id": 177, "pretty_name": "placeholder"},
    "NPC_MERMAID_MAGIC_FLARE"           : {"id": 181, "pretty_name": "placeholder"},
    "NPC_MERMAID_QUEEN"                 : {"id": 182, "pretty_name": "placeholder"},
    "NPC_MERMAID_STATUE_GHOST_SHIP"     : {"id": 185, "pretty_name": "placeholder"},
    "NPC_DOLPHIN_SECRET_CAVE"           : {"id": 187, "pretty_name": "placeholder"},
    "NPC_MERMAID7"                      : {"id": 189, "pretty_name": "placeholder"},
    "NPC_ANGELFISH4"                    : {"id": 190, "pretty_name": "placeholder"},
    "NPC_MERMAID8"                      : {"id": 192, "pretty_name": "placeholder"},
    "NPC_DOLPHIN_PEARL"                 : {"id": 193, "pretty_name": "placeholder"},
    "NPC_MERMAID9"                      : {"id": 194, "pretty_name": "placeholder"},
    "NPC_GRANDPA"                       : {"id": 201, "pretty_name": "placeholder"},
    "NPC_GIRL"                          : {"id": 202, "pretty_name": "placeholder"},
    "NPC_MUSHROOM"                      : {"id": 203, "pretty_name": "placeholder"},
    "NPC_BOY"                           : {"id": 204, "pretty_name": "placeholder"},
    "NPC_GRANDPA2"                      : {"id": 211, "pretty_name": "placeholder"},
    "NPC_SNAIL_JOCKEY"                  : {"id": 212, "pretty_name": "placeholder"},
    "NPC_NOME"                          : {"id": 214, "pretty_name": "placeholder"},
    "NPC_BOY2"                          : {"id": 215, "pretty_name": "placeholder"},
    "NPC_MUSHROOM_EMBLEM_F"             : {"id": 221, "pretty_name": "placeholder"},
    "NPC_DANCING_GRANDMA"               : {"id": 225, "pretty_name": "placeholder"},
    "NPC_DANCING_GRANDMA2"              : {"id": 230, "pretty_name": "placeholder"},
    "NPC_SNAIL_EMBLEM_E"                : {"id": 232, "pretty_name": "placeholder"},
    "NPC_BOY_MUSHROOM_SHOES"            : {"id": 233, "pretty_name": "placeholder"},
    "NPC_GRANDMA"                       : {"id": 234, "pretty_name": "placeholder"},
    "NPC_GIRL2"                         : {"id": 235, "pretty_name": "placeholder"},
    "NPC_MUSHROOM2"                     : {"id": 238, "pretty_name": "placeholder"},
    "NPC_SNAIL_RACER"                   : {"id": 239, "pretty_name": "placeholder"},
    "NPC_SNAIL_RACER2"                  : {"id": 240, "pretty_name": "placeholder"},
    "NPC_GIRL3"                         : {"id": 242, "pretty_name": "placeholder"},
    "NPC_MUSHROOM3"                     : {"id": 246, "pretty_name": "placeholder"},
    "NPC_SNAIL"                         : {"id": 247, "pretty_name": "placeholder"},
    "NPC_GRANDPA3"                      : {"id": 248, "pretty_name": "placeholder"},
    "NPC_SNAIL2"                        : {"id": 250, "pretty_name": "placeholder"},
    "NPC_GRANDPA4"                      : {"id": 252, "pretty_name": "placeholder"},
    "NPC_GRANDPA_LUNE"                  : {"id": 254, "pretty_name": "placeholder"},
    "NPC_GRANDPA5"                      : {"id": 255, "pretty_name": "placeholder"},
    "NPC_MOUNTAIN_KING"                 : {"id": 259, "pretty_name": "placeholder"},
    "NPC_PLANT_HERB"                    : {"id": 265, "pretty_name": "placeholder"},
    "NPC_PLANT"                         : {"id": 267, "pretty_name": "placeholder"},
    "NPC_CHEST_OF_DRAWERS_MYSTIC_ARMOR" : {"id": 268, "pretty_name": "placeholder"},
    "NPC_CAT"                           : {"id": 269, "pretty_name": "placeholder"},
    "NPC_GREAT_DOOR_ZANTETSU_SWORD"     : {"id": 274, "pretty_name": "placeholder"},
    "NPC_CAT2"                          : {"id": 276, "pretty_name": "placeholder"},
    "NPC_GREAT_DOOR"                    : {"id": 282, "pretty_name": "placeholder"},
    "NPC_CAT3"                          : {"id": 283, "pretty_name": "placeholder"},
    "NPC_MODEL_TOWN1"                   : {"id": 286, "pretty_name": "placeholder"},
    "NPC_GREAT_DOOR_MODEL_TOWNS"        : {"id": 288, "pretty_name": "placeholder"},
    "NPC_STEPS_UPSTAIRS"                : {"id": 290, "pretty_name": "placeholder"},
    "NPC_CAT_DOOR_KEY"                  : {"id": 294, "pretty_name": "placeholder"},
    "NPC_MOUSE"                         : {"id": 297, "pretty_name": "placeholder"},
    "NPC_MARIE"                         : {"id": 303, "pretty_name": "placeholder"},
    "NPC_DOLL"                          : {"id": 310, "pretty_name": "placeholder"},
    "NPC_CHEST_OF_DRAWERS"              : {"id": 311, "pretty_name": "placeholder"},
    "NPC_PLANT2"                        : {"id": 313, "pretty_name": "placeholder"},
    "NPC_MOUSE2"                        : {"id": 315, "pretty_name": "placeholder"},
    "NPC_MOUSE_SPARK_BOMB"              : {"id": 316, "pretty_name": "placeholder"},
    "NPC_MOUSE3"                        : {"id": 318, "pretty_name": "placeholder"},
    "NPC_GREAT_DOOR_SOUL_OF_DETECTION"  : {"id": 322, "pretty_name": "placeholder"},
    "NPC_MODEL_TOWN2"                   : {"id": 325, "pretty_name": "placeholder"},
    "NPC_MOUSE4"                        : {"id": 330, "pretty_name": "placeholder"},
    "NPC_STEPS_MARIE"                   : {"id": 331, "pretty_name": "placeholder"},
    "NPC_CHEST_OF_DRAWERS2"             : {"id": 332, "pretty_name": "placeholder"},
    "NPC_PLANT_ACTINIDIA_LEAVES"        : {"id": 333, "pretty_name": "placeholder"},
    "NPC_MOUSE5"                        : {"id": 338, "pretty_name": "placeholder"},
    "NPC_CAT4"                          : {"id": 339, "pretty_name": "placeholder"},
    "NPC_STAIRS_POWER_PLANT"            : {"id": 341, "pretty_name": "placeholder"},
    "NPC_SOLDIER"                       : {"id": 345, "pretty_name": "placeholder"},
    "NPC_SOLDIER2"                      : {"id": 346, "pretty_name": "placeholder"},
    "NPC_SOLDIER3"                      : {"id": 351, "pretty_name": "placeholder"},
    "NPC_SOLDIER_ELEMENTAL_MAIL"        : {"id": 353, "pretty_name": "placeholder"},
    "NPC_SOLDIER4"                      : {"id": 354, "pretty_name": "placeholder"},
    "NPC_SOLDIER5"                      : {"id": 358, "pretty_name": "placeholder"},
    "NPC_SINGER_CONCERT_HALL"           : {"id": 359, "pretty_name": "placeholder"},
    "NPC_SOLDIER6"                      : {"id": 360, "pretty_name": "placeholder"},
    "NPC_MAID"                          : {"id": 363, "pretty_name": "placeholder"},
    "NPC_SOLDIER_LEFT_TOWER"            : {"id": 365, "pretty_name": "placeholder"},
    "NPC_SOLDIER_DOK"                   : {"id": 366, "pretty_name": "placeholder"},
    "NPC_SOLDIER_PLATINUM_CARD"         : {"id": 368, "pretty_name": "placeholder"},
    "NPC_SINGER"                        : {"id": 370, "pretty_name": "placeholder"},
    "NPC_SOLDIER_SOUL_OF_REALITY"       : {"id": 377, "pretty_name": "placeholder"},
    "NPC_MAID2"                         : {"id": 382, "pretty_name": "placeholder"},
    "NPC_QUEEN_MAGRIDD"                 : {"id": 383, "pretty_name": "placeholder"},
    "NPC_SOLDIER_WITH_LEO"              : {"id": 385, "pretty_name": "placeholder"},
    "NPC_SOLDIER_RIGHT_TOWER"           : {"id": 386, "pretty_name": "placeholder"},
    "NPC_DR_LEO"                        : {"id": 387, "pretty_name": "placeholder"},
    "NPC_SOLDIER7"                      : {"id": 389, "pretty_name": "placeholder"},
    "NPC_SOLDIER8"                      : {"id": 390, "pretty_name": "placeholder"},
    "NPC_MAID_HERB"                     : {"id": 391, "pretty_name": "placeholder"},
    "NPC_SOLDIER_CASTLE"                : {"id": 396, "pretty_name": "placeholder"},
    "NPC_SOLDIER9"                      : {"id": 397, "pretty_name": "placeholder"},
    "NPC_SOLDIER10"                     : {"id": 399, "pretty_name": "placeholder"},
    "NPC_SOLDIER11"                     : {"id": 402, "pretty_name": "placeholder"},
    "NPC_KING_MAGRIDD"                  : {"id": 405, "pretty_name": "placeholder"},
}

KEY_ITEMS = [
    "SWORD_OF_LIFE"  ,
    "PSYCHO_SWORD"   ,
    "CRITICAL_SWORD" ,
    "LUCKY_BLADE"    ,
    "ZANTETSU_SWORD" ,
    "SPIRIT_SWORD"   ,
    "RECOVERY_SWORD" ,
    "SOUL_BLADE"     ,
    "IRON_ARMOR"     ,
    "ICE_ARMOR"      ,
    "BUBBLE_ARMOR"   ,
    "MAGIC_ARMOR"    ,
    "MYSTIC_ARMOR"   ,
    "LIGHT_ARMOR"    ,
    "ELEMENTAL_MAIL" ,
    "SOUL_ARMOR"     ,
    "FLAME_BALL"     ,
    "LIGHT_ARROW"    ,
    "MAGIC_FLARE"    ,
    "ROTATOR"        ,
    "SPARK_BOMB"     ,
    "FLAME_PILLAR"   ,
    "TORNADO"        ,
    "PHOENIX"        ,
    "GOATS_FOOD"     ,
    "HARP_STRING"    ,
    "PASS"           ,
    "DREAM_ROD"      ,
    "LEOS_BRUSH"     ,
    "GREENWOOD_LEAF" ,
    "MOLES_RIBBON"   ,
    "BIG_PEARL"      ,
    "MERMAIDS_TEARS" ,
    "MUSHROOM_SHOES" ,
    "MOBILE_KEY"     ,
    "THUNDER_RING"   ,
    "DELICIOUS_SEEDS",
    "ACTINIDIA_LEAF" ,
    "DOOR_KEY"       ,
    "PLATINUM_CARD"  ,
    "VIP_CARD"       ,
    "EMBLEM_A"       ,
    "EMBLEM_B"       ,
    "EMBLEM_C"       ,
    "EMBLEM_D"       ,
    "EMBLEM_E"       ,
    "EMBLEM_F"       ,
    "EMBLEM_G"       ,
    "EMBLEM_H"       ,
    "RED_HOT_MIRROR" ,
    "RED_HOT_BALL"   ,
    "RED_HOT_STICK"  ,
    "POWER_BRACELET" ,
    "SHIELD_BRACELET",
    "SUPER_BRACELET" ,
    "BROWN_STONE"    ,
    "GREEN_STONE"    ,
    "BLUE_STONE"     ,
    "SILVER_STONE"   ,
    "PURPLE_STONE"   ,
    "BLACK_STONE"    ,
    "MAGIC_BELL"     ,
]

REGIONS = {
	0: {
        "detail": "Region 0 - Act 1 start, Underground Castle before elevator",
        "description": "Underground Castle",
		"checks": [ 
			{"type": "chest", "id": 0}, # SWORD_OF_LIFE
			{"type": "item", "name": "ITEM_MAGICIAN"},
			{"type": "lair", "name": "NPC_OLD_WOMAN"},
			{"type": "lair", "name": "NPC_TOOL_SHOP_OWNER"},
			{"type": "lair", "name": "NPC_TULIP"},
			{"type": "lair", "name": "NPC_BRIDGE_GUARD"},
			{"type": "lair", "name": "NPC_IVY_CHEST_ROOM"},
			{"type": "lair", "name": "NPC_WATER_MILL"},
			{"type": "chest", "id": 3}, # GEMS_EXP 12
			{"type": "chest", "id": 4}, # MEDICAL_HERB
			{"type": "chest", "id": 5}, #"name": "CHEST_DREAM_ROD"},
			{"type": "item", "name": "ITEM_CRYSTAL_UNDERGROUND_CASTLE"},
		],
		"requirements": [],
		"act": 1,
        "is_act_hub": True,
        "connected_regions": [1, 2, 3, 4, 5, 42, 43, 44, 45, 46, 47, 48]
	},
	1: {
        "detail": "Region 1 - Underground chest room",
        "description": "Grass Valley",
        "checks": [ 
			{"type": "chest", "id": 1}, # IRON_ARMOR
			{"type": "chest", "id": 2}, # GEMS_EXP 50
			{"type": "item", "name": "ITEM_CRYSTAL_GRASS_VALLEY"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_IVY_CHEST_ROOM"},
        ],
        "act": 1
    },
	2: {
        "detail": "Region 2 - Underground Castle after elevator",
        "description": "Underground Castle",
        "checks": [ 
			{"type": "lair", "name": "NPC_OLD_MAN2"}, 
			{"type": "lair", "name": "NPC_GOAT_HERB"},
			{"type": "lair", "name": "NPC_LISA"}, 
			{"type": "lair", "name": "NPC_TULIP2"}, 
			{"type": "lair", "name": "NPC_ARCHITECT"}, 
			{"type": "lair", "name": "NPC_IVY2"}, 
			{"type": "lair", "name": "NPC_TEDDY"}, 
			{"type": "lair", "name": "NPC_GOAT"}, 
			{"type": "lair", "name": "NPC_TULIP3"}, 
			{"type": "lair", "name": "NPC_LEOS_HOUSE"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_WATER_MILL"},
        ],
        "act": 1
    },
	3: {
        "detail": "Region 3 - Leo's Paintings",
        "description": "Leo`s Paintings",
        "checks": [ 
			{"type": "lair", "name": "NPC_TULIP4"}, 
			{"type": "lair", "name": "NPC_LONELY_GOAT"}, 
			{"type": "lair", "name": "NPC_IVY"}, 
			{"type": "lair", "name": "NPC_GOAT2"}, 
			{"type": "lair", "name": "NPC_BOY_CABIN"}, 
			{"type": "lair", "name": "NPC_TULIP_PASS"}, 
			{"type": "lair", "name": "NPC_BOY_CAVE"}, 
			{"type": "lair", "name": "NPC_VILLAGE_CHIEF"}, 
			{"type": "chest", "id": 7}, # MEDICAL_HERB
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_ARCHITECT"},
            {"type": "npc_id", "name": "NPC_LEOS_HOUSE"},
            {"type": "item", "name": "LEOS_BRUSH"},
        ],
        "act": 1
    },
	4: {
        "detail": "Region 4 - Last part of Underground Castle",
        "description": "Underground Castle",
        "checks": [ 
			{"type": "lair", "name": "NPC_OLD_MAN"}, 
			{"type": "chest", "id": 6}, #"name": "CHEST_LEOS_BRUSH"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_LISA"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 1
    },
	5: {
        "detail": "Region 5 - Leo's Paintings Metal Enemies",
        "description": "Leo`s Paintings",
        "checks": [ 
			{"type": "lair", "name": "NPC_IVY_EMBLEM_A"}, 
			{"type": "lair", "name": "NPC_IVY_RECOVERY_SWORD"}, 
			{"type": "chest", "id": 8}, # TORNADO
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_metal"},
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_ARCHITECT"},
            {"type": "npc_id", "name": "NPC_LEOS_HOUSE"},
            {"type": "item", "name": "LEOS_BRUSH"},
        ],
        "act": 1
    },
    # Removed this section because it is essentially the same as being in the beginning of act 2.
    # # Region 6 - Final part of Act 1. Get item from mayor and start Act 2.
	# 6: {
    #     "checks": [ 
	# 		{"type": "npc_id", "name": "ITEM_VILLAGE_CHIEF"}, 
    #     ],
    #     "requirements": [ 
    #         {"type": "npc_id", "name": "NPC_VILLAGE_CHIEF"},
    #         {"type": "npc_id", "name": "NPC_OLD_WOMAN"},
    #     ],
    #     "act": 1,
    # },
	6: {
        "detail": "Region 6 - Act 2 start, Lost Marshes + Water/Fire Shrines",
        "description": "Lost Marshes",
        "checks": [ 
			{"type": "item", "name": "ITEM_VILLAGE_CHIEF"}, 
			{"type": "lair", "name": "NPC_BIRD"}, 
			{"type": "lair", "name": "NPC_DOG"}, 
			{"type": "lair", "name": "NPC_SQUIRREL_PSYCHO_SWORD"}, 
			{"type": "lair", "name": "NPC_BIRD2"}, 
			{"type": "lair", "name": "NPC_MOLE_SOUL_OF_LIGHT"}, 
			{"type": "lair", "name": "NPC_CROCODILE"}, 
			{"type": "lair", "name": "NPC_SQUIRREL"}, 
			{"type": "lair", "name": "NPC_MOLE"}, 
			{"type": "lair", "name": "NPC_DEER"}, 
			{"type": "lair", "name": "NPC_DOG2"}, 
			{"type": "lair", "name": "NPC_DOG4"}, 
			{"type": "lair", "name": "NPC_DOG5"}, 
			{"type": "lair", "name": "NPC_CROCODILE2"}, 
			{"type": "lair", "name": "NPC_SQUIRREL_ICE_ARMOR"}, 
			{"type": "lair", "name": "NPC_MOLE2"}, 
			{"type": "lair", "name": "NPC_SQUIRREL3"}, 
			{"type": "lair", "name": "NPC_BIRD_GREENWOOD_LEAF"}, 
			{"type": "lair", "name": "NPC_MOLE3"}, 
			{"type": "lair", "name": "NPC_DEER_MAGIC_BELL"}, 
			{"type": "lair", "name": "NPC_SQUIRREL2"}, 
			{"type": "chest", "id": 11}, # GEMS_EXP 50
			{"type": "chest", "id": 12}, # GEMS_EXP 150
			{"type": "chest", "id": 13}, # MEDICAL_HERB
			{"type": "chest", "id": 14}, # DELICIOUS_SEEDS
			{"type": "chest", "id": 15}, # GEMS_EXP 50
			{"type": "chest", "id": 16}, # MEDICAL_HERB
			# {"type": "chest", "id": 17}, # NOTHING # WARNING: this (normally empty) chest can disappear!!!
			{"type": "chest", "id": 19}, # GEMS_EXP 100
			{"type": "chest", "id": 20}, # GEMS_EXP 60
			{"type": "item", "name": "ITEM_CRYSTAL_WATER_SHRINE"}, 
			{"type": "item", "name": "ITEM_WATER_SHRINE_TILE"}, 
			{"type": "item", "name": "ITEM_CRYSTAL_LIGHT_ARROW"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_VILLAGE_CHIEF"},
            {"type": "npc_id", "name": "NPC_OLD_WOMAN"},
        ],
        "act": 2,
        "is_act_hub": True,
        "connected_regions": [7, 8, 9, 10, 11, 49, 50, 51, 52, 53, 54]
    },
	7: {
        "detail": "Region 7 - Last part of Marshes + Light Shrine",
        "description": "Lost Marshes",
        "checks": [ 
			{"type": "lair", "name": "NPC_MOLE_SHIELD_BRACELET"}, 
			{"type": "lair", "name": "NPC_DOG3"}, 
			{"type": "lair", "name": "NPC_SQUIRREL_EMBLEM_C"}, 
			{"type": "lair", "name": "NPC_CROCODILE3"}, 
			{"type": "lair", "name": "NPC_MONMO"}, 
			{"type": "lair", "name": "NPC_GREENWOODS_GUARDIAN"}, 
			{"type": "item", "name": "ITEM_CRYSTAL_LOST_MARSH"}, 
        ],
        "requirements": [ 
            {"type": "item", "name": "GREENWOOD_LEAF"},
        ],
        "act": 2
    },
	8: {
        "detail": "Region 8 - Fire Shrine Scorpions",
        "description": "Lost Marshes",
        "checks": [ 
			{"type": "lair", "name": "NPC_BIRD3"}, 
			{"type": "chest", "id": 18}, 
			{"type": "item", "name": "ITEM_CRYSTAL_FIRE_SHRINE"}, 
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_metal"},
        ],
        "act": 2
    },
	9: {
        "detail": "Region 9 - Monmo's Treasure",
        "description": "Greenwood",
        "checks": [ 
			{"type": "chest", "id": 10}, # MOLES_RIBBON
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MONMO"},
            {"type": "npc_id", "name": "NPC_MOLE3"},
        ],
        "act": 2
    },
	10: {
        "detail": "Region 10 - Ice Armor chest",
        "description": "Greenwood",
        "checks": [ 
			{"type": "chest", "id": 9}, # ICE_ARMOR
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MOLE"},
            {"type": "npc_id", "name": "NPC_SQUIRREL_ICE_ARMOR"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 2
    },
	11: {
        "detail": "Region 11 - Light Shrine Fire Spirits",
        "description": "Lost Marshes",
        "checks": [ 
			{"type": "lair", "name": "NPC_BIRD_RED_HOT_MIRROR"}, 
			{"type": "chest", "id": 21}, # FLAME_PILLAR
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_spirit"},
            {"type": "item", "name": "GREENWOOD_LEAF"},
       ],
        "act": 2
    },
	12: {
        "detail": "Region 12 - Act 3 start, Southerta",
        "description": "Southerta",
        "checks": [ 
			{"type": "item", "name": "ITEM_GREENWOODS_GUARDIAN"}, 
			{"type": "lair", "name": "NPC_DOLPHIN2"}, 
			{"type": "lair", "name": "NPC_MERMAID4"}, 
			{"type": "lair", "name": "NPC_MERMAID5"}, 
			{"type": "lair", "name": "NPC_MERMAID6"}, 
			{"type": "lair", "name": "NPC_MERMAID_BUBBLE_ARMOR"}, 
			{"type": "chest", "id": 28}, # MEDICAL_HERB
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREENWOODS_GUARDIAN"},
       ],
        "act": 3,
        "is_act_hub": True,
        "connected_regions": [13, 14, 15, 16, 17, 18, 77, 19, 20, 21, 55, 56, 57, 58, 59]
    },
	13: {
        "detail": "Region 13 - Last soul of Southerta",
        "description": "Southerta",
        "checks": [ 
			{"type": "lair", "name": "NPC_MERMAID_STATUE_ROCKBIRD"}, 
        ],
        "requirements": [ 
            {"type": "item", "name": "BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	14: {
        "detail": "Region 14 - Big Pearl chest",
        "description": "Seabed",
        "checks": [ 
			{"type": "chest", "id": 23}, #"name": "CHEST_BIG_PEARL"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_PEARL"},
            {"type": "npc_id", "name": "NPC_DOLPHIN_PEARL"},
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	15: {
        "detail": "Region 15 - Rockbird",
        "description": "Rockbird",
        "checks": [ 
			{"type": "lair", "name": "NPC_MERMAID9"}, 
			{"type": "lair", "name": "NPC_MERMAID_TEARS"}, 
			{"type": "lair", "name": "NPC_MERMAID_MAGIC_FLARE"}, 
			{"type": "lair", "name": "NPC_ANGELFISH_SOUL_OF_SHIELD"}, 
			{"type": "lair", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
			{"type": "chest", "id": 29}, # MEDICAL_HERB
			{"type": "chest", "id": 30}, # GEMS_EXP 60
			{"type": "item", "name": "ITEM_CRYSTAL_ROCKBIRD"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_ROCKBIRD"},
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	16: {
        "detail": "Region 16 - Blester",
        "description": "Blester",
        "checks": [ 
			{"type": "lair", "name": "NPC_ANGELFISH"}, 
			{"type": "lair", "name": "NPC_ANGELFISH2"}, 
			{"type": "lair", "name": "NPC_MERMAID"}, 
			{"type": "lair", "name": "NPC_MERMAID7"}, 
			{"type": "lair", "name": "NPC_ANGELFISH4"}, 
			{"type": "lair", "name": "NPC_MERMAID8"}, 
			{"type": "lair", "name": "NPC_DOLPHIN_SECRET_CAVE"}, 
			{"type": "item", "name": "ITEM_CRYSTAL_SEABED_NEAR_BLESTER"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_BLESTER"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	17: {
        "detail": "Region 17 - Blester Metal Gorillas",
        "description": "Blester",
        "checks": [ 
			{"type": "lair", "name": "NPC_MERMAID_STATUE_GHOST_SHIP"}, 
        ],
        "contains_groups": True,
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_BLESTER"}, 
            {"type": "flag", "name": "has_thunder"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	18: { # Split into 77 to allow for mermaid's tears requirement
        "detail": "Region 18 - Durean",
        "description": "Durean",
        "checks": [ 
			{"type": "lair", "name": "NPC_DOLPHIN_PEARL"}, 
			{"type": "lair", "name": "NPC_LUE"}, 
			# {"type": "lair", "name": "NPC_MERMAID_PEARL"}, 
			{"type": "lair", "name": "NPC_MERMAID2"}, 
			{"type": "lair", "name": "NPC_MERMAID_NANA"}, 
			{"type": "lair", "name": "NPC_DOLPHIN_SAVES_LUE"}, 
			{"type": "lair", "name": "NPC_MERMAID3"}, 
			# {"type": "lair", "name": "NPC_MERMAID_STATUE_BLESTER"}, 
			# {"type": "chest", "id": 31}, # CRITICAL_SWORD
			{"type": "chest", "id": 32}, # STRANGE_BOTTLE
			{"type": "item", "name": "ITEM_CRYSTAL_SEABED_NEAR_DUREAN"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
            # {"type": "item", "name": "MERMAIDS_TEARS"}, # Opted not to make this required.
       ],
        "act": 3
    },
	19: {
        "detail": "Region 19 - Durean Metal Gorillas",
        "description": "Durean",
        "checks": [ 
			{"type": "lair", "name": "NPC_MERMAID_RED_HOT_STICK"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
            {"type": "flag", "name": "can_cut_metal"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	20: {
        "detail": "Region 20 - Ghost Ship",
        "description": "Ghost Ship",
        "checks": [ 
			{"type": "lair", "name": "NPC_ANGELFISH3"}, 
			{"type": "lair", "name": "NPC_DOLPHIN"}, 
			{"type": "lair", "name": "NPC_MERMAID_QUEEN"}, 
			{"type": "chest", "id": 33}, # GEMS_EXP 1
			{"type": "chest", "id": 34}, # POWER_BRACELET
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_GHOST_SHIP"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
	21: {
        "detail": "Region 21 - Seabed Secret Cave",
        "description": "Seabed",
        "checks": [ 
			{"type": "chest", "id": 24}, # EMBLEM_D
			{"type": "chest", "id": 25}, # GEMS_EXP 80
			{"type": "chest", "id": 26}, # MEDICAL_HERB
			{"type": "chest", "id": 27}, # NOTHING
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_PEARL"}, 
            {"type": "npc_id", "name": "NPC_DOLPHIN_SECRET_CAVE"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_GHOST_SHIP"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
            {"type": "item", "name": "DREAM_ROD"}, 
            {"type": "item", "name": "BIG_PEARL"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
       ],
        "act": 3
    },
    # Region 22 - Used to be Mermaid's Tears chest, now useless (previously region 23)
    # Region ^ was never neaded. I'm leaving a space here JIC.
	23: {
        "detail": "Region 23 - Act 4 start, Mountain of Souls",
        "description": "Mountain of Souls",
        "checks": [ 
			{"type": "item", "name": "ITEM_MERMAID_QUEEN"}, 
			{"type": "lair", "name": "NPC_GIRL"}, 
			{"type": "lair", "name": "NPC_GRANDPA"}, 
			{"type": "lair", "name": "NPC_MUSHROOM"}, 
			{"type": "lair", "name": "NPC_BOY"}, 
			{"type": "lair", "name": "NPC_GRANDPA2"}, 
			{"type": "lair", "name": "NPC_SNAIL_JOCKEY"}, 
			{"type": "lair", "name": "NPC_BOY_MUSHROOM_SHOES"}, 
			{"type": "lair", "name": "NPC_GIRL2"}, 
			{"type": "chest", "id": 35}, 
			{"type": "chest", "id": 36}, 
			{"type": "chest", "id": 37}, 
			{"type": "chest", "id": 38}, 
			{"type": "chest", "id": 39}, 
			{"type": "item", "name": "ITEM_CRYSTAL_MOUNTAIN_OF_SOULS"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_QUEEN"},
       ],
        "act": 4,
        "is_act_hub": True,
        "connected_regions": [24, 25, 40, 60, 61, 62]
    },
	24: {
        "detail": "Region 24 - Mountain of Souls last lair + Laynole",
        "description": "Laynole",
        "checks": [ 
			{"type": "lair", "name": "NPC_GRANDMA"}, 
			{"type": "lair", "name": "NPC_MUSHROOM2"}, 
			{"type": "lair", "name": "NPC_SNAIL_RACER"}, 
			{"type": "lair", "name": "NPC_SNAIL_RACER2"}, 
			{"type": "lair", "name": "NPC_GIRL3"}, 
			{"type": "lair", "name": "NPC_MUSHROOM3"}, 
			{"type": "lair", "name": "NPC_SNAIL"}, 
			{"type": "lair", "name": "NPC_GRANDPA3"}, 
			{"type": "lair", "name": "NPC_GRANDPA4"}, 
			{"type": "lair", "name": "NPC_GRANDPA_LUNE"}, 
			{"type": "lair", "name": "NPC_SNAIL2"}, 
			{"type": "lair", "name": "NPC_GRANDPA5"}, 
			{"type": "chest", "id": 40,}, #"name": "CHEST_LUCKY_BLADE"}, 
        ],
        "requirements": [ 
            {"type": "item", "name": "MUSHROOM_SHOES"},
       ],
        "act": 4,
    },
	25: {
        "detail": "Region 25 - Last part of Laynole + Lune",
        "description": "Lune",
        "checks": [ 
			{"type": "lair", "name": "NPC_BOY2"}, 
			{"type": "lair", "name": "NPC_NOME"}, 
			{"type": "lair", "name": "NPC_MUSHROOM_EMBLEM_F"}, 
			{"type": "lair", "name": "NPC_DANCING_GRANDMA"}, 
			{"type": "lair", "name": "NPC_DANCING_GRANDMA2"}, 
			{"type": "lair", "name": "NPC_MOUNTAIN_KING"}, 
			{"type": "chest", "id": 41}, # STRANGE_BOTTLE
			{"type": "chest", "id": 42}, # ROTATOR
			{"type": "item", "name": "ITEM_CRYSTAL_LUNE"}, 
        ],
        "requirements": [ 
            {"type": "item", "name": "LUCKY_BLADE"},
            {"type": "npc_id", "name": "NPC_GIRL3"},
            {"type": "npc_id", "name": "NPC_GRANDPA4"},
            {"type": "npc_id", "name": "NPC_GRANDPA_LUNE"},
       ],
        "act": 4,
    },
	26: {
        "detail": "Region 26 - Act 5 start, first lairs of Leo's Lab Basement",
        "description": "Lab Basement",
        "checks": [ 
			{"type": "lair", "name": "NPC_PLANT"}, 
			{"type": "lair", "name": "NPC_CAT"}, 
			{"type": "lair", "name": "NPC_GREAT_DOOR_ZANTETSU_SWORD"}, 
			{"type": "item", "name": "ITEM_NOME"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GIRL3"},
            {"type": "npc_id", "name": "NPC_GRANDPA4"},
            {"type": "npc_id", "name": "NPC_MUSHROOM2"},
            {"type": "npc_id", "name": "NPC_GRANDPA5"},
            {"type": "npc_id", "name": "NPC_NOME"},
            {"type": "npc_id", "name": "NPC_MOUNTAIN_KING"},
       ],
        "act": 5,
        "is_act_hub": True,
        "connected_regions": [27, 66, 28, 29, 30, 31, 32, 63, 64, 65, 67, 68]
    },
	27: { # Split into 66 to allow for separate ice armor requirements
        "detail": "Region 27 - Leo's Lab Basement 1",
        "description": "Lab Basement",
        "checks": [ 
			{"type": "lair", "name": "NPC_PLANT_HERB"}, 
			{"type": "lair", "name": "NPC_CAT2"}, 
			{"type": "lair", "name": "NPC_CAT3"}, 
			{"type": "lair", "name": "NPC_GREAT_DOOR"}, 
			{"type": "lair", "name": "NPC_CHEST_OF_DRAWERS_MYSTIC_ARMOR"}, 
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_metal"},
       ],
        "act": 5,
    },
	28: {
        "detail": "Region 28 - Leo's Lab main room",
        "description": "Leo`s Lab",
        "checks": [ 
			{"type": "chest", "id": 43}, # ZANTETSU_SWORD
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_ZANTETSU_SWORD"},
       ],
        "act": 5,
    },
	29: {
        "detail": "Region 29 - Model Town 1",
        "description": "Model Town",
        "checks": [ 
			{"type": "lair", "name": "NPC_CHEST_OF_DRAWERS"}, 
			{"type": "lair", "name": "NPC_PLANT2"}, 
			{"type": "lair", "name": "NPC_MOUSE2"}, 
			{"type": "lair", "name": "NPC_MOUSE3"}, 
			{"type": "lair", "name": "NPC_MOUSE4"}, 
			{"type": "lair", "name": "NPC_MOUSE_SPARK_BOMB"}, 
			{"type": "lair", "name": "NPC_GREAT_DOOR_SOUL_OF_DETECTION"}, 
			{"type": "lair", "name": "NPC_MODEL_TOWN2"}, 
			{"type": "lair", "name": "NPC_STEPS_MARIE"}, 
			{"type": "chest", "id": 45}, # GEMS_EXP 50
			{"type": "chest", "id": 46}, # MEDICAL_HERB
			{"type": "chest", "id": 47}, # GEMS_EXP 80
			{"type": "item", "name": "ITEM_CRYSTAL_MODEL_TOWN"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MODEL_TOWN1"},
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "flag", "name": "has_magic"},
       ],
        "act": 5,
    },
    30: {
        "detail": "Region 30 - Model Town 2",
        "description": "Model Town",
        "checks": [ 
			{"type": "lair", "name": "NPC_CHEST_OF_DRAWERS2"}, 
			{"type": "lair", "name": "NPC_PLANT_ACTINIDIA_LEAVES"}, 
			{"type": "lair", "name": "NPC_MOUSE5"}, 
			{"type": "lair", "name": "NPC_CAT4"}, 
			{"type": "lair", "name": "NPC_STAIRS_POWER_PLANT"}, 
			{"type": "chest", "id": 48}, # STRANGE_BOTTLE
			{"type": "chest", "id": 49}, # MEDICAL_HERB
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MODEL_TOWN2"},
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "flag", "name": "has_magic"},
       ],
        "act": 5,
    },
    31: {
        "detail": "Region 31 - Light Armor chest",
        "description": "Power Plant",
        "checks": [ 
			{"type": "chest", "id": 44}, # LIGHT_ARMOR
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_STAIRS_POWER_PLANT"},
            {"type": "flag", "name": "can_cut_metal"},
       ],
        "act": 5,
    },
    32: {
        "detail": "Region 32 - Power Plant",
        "description": "Power Plant",
        "checks": [ 
			{"type": "lair", "name": "NPC_DOLL"}, 
			{"type": "lair", "name": "NPC_MARIE"}, 
			{"type": "item", "name": "ITEM_CRYSTAL_POWER_PLANT"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_STAIRS_POWER_PLANT"},
            {"type": "flag", "name": "can_cut_metal"},
        ],
        "act": 5,
    },
    33: {
        "detail": "Region 33 - Act 6 start, first lairs of Magridd Castle Basement",
        "description": "Castle Basement",
        "checks": [ 
			{"type": "item", "name": "ITEM_MARIE"}, 
			{"type": "lair", "name": "NPC_SOLDIER"}, 
			{"type": "chest", "id": 50}, # GEMS_EXP 80
			{"type": "chest", "id": 51}, # SPIRIT_SWORD
			{"type": "item", "name": "ITEM_HARP_STRING"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MARIE"},
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "npc_id", "name": "NPC_STEPS_MARIE"},
        ],
        "act": 6,
        "is_act_hub": True,
        "connected_regions": [34, 35, 36, 38, 69, 71, 72, 73, 74, 75, 76, 78]
    },
    34: {
        "detail": "Region 34 - Magridd Castle Basement",
        "description": "Castle Basement",
        "checks": [ 
			{"type": "lair", "name": "NPC_SOLDIER2"}, 
			{"type": "lair", "name": "NPC_SINGER_CONCERT_HALL"}, 
			{"type": "lair", "name": "NPC_SOLDIER3"}, 
			{"type": "lair", "name": "NPC_SOLDIER4"}, 
			{"type": "lair", "name": "NPC_SOLDIER5"}, 
			{"type": "lair", "name": "NPC_SOLDIER6"}, 
			{"type": "lair", "name": "NPC_SOLDIER_ELEMENTAL_MAIL"}, 
			{"type": "lair", "name": "NPC_MAID"}, 
			{"type": "lair", "name": "NPC_SOLDIER_LEFT_TOWER"}, 
			{"type": "lair", "name": "NPC_SOLDIER_DOK"}, 
			{"type": "lair", "name": "NPC_SOLDIER_PLATINUM_CARD"}, 
			{"type": "lair", "name": "NPC_SINGER"}, 
			{"type": "chest", "id": 52}, # STRANGE_BOTTLE
			{"type": "chest", "id": 53}, # MEDICAL_HERB
			{"type": "chest", "id": 54}, # GEMS_EXP 100
			{"type": "chest", "id": 55}, # EMBLEM_B
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_spirit"},
        ],
        "act": 6,
    },
    35: {
        "detail": "Region 35 - Magridd Castle Left Tower",
        "description": "Castle Tower",
        "checks": [ 
			{"type": "lair", "name": "NPC_SOLDIER_SOUL_OF_REALITY"}, 
			{"type": "lair", "name": "NPC_QUEEN_MAGRIDD"}, 
			{"type": "lair", "name": "NPC_MAID2"}, 
			{"type": "lair", "name": "NPC_SOLDIER_WITH_LEO"}, 
			{"type": "lair", "name": "NPC_SOLDIER_RIGHT_TOWER"}, 
			{"type": "lair", "name": "NPC_DR_LEO"}, 
			{"type": "lair", "name": "NPC_SOLDIER7"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_LEFT_TOWER"},
            {"type": "item", "name": "PLATINUM_CARD"},
        ],
        "act": 6,
    },
    36: {
        "detail": "Region 36 - Magridd Castle Right Tower",
        "description": "Castle Tower",
        "checks": [ 
			{"type": "lair", "name": "NPC_MAID_HERB"}, 
			{"type": "lair", "name": "NPC_SOLDIER8"}, 
			{"type": "lair", "name": "NPC_SOLDIER_CASTLE"}, 
			{"type": "lair", "name": "NPC_SOLDIER9"}, 
			{"type": "lair", "name": "NPC_SOLDIER10"}, 
			{"type": "lair", "name": "NPC_SOLDIER11"}, 
			{"type": "chest", "id": 56}, # GEMS_EXP 80
			{"type": "chest", "id": 57}, # GEMS_EXP 80
			{"type": "chest", "id": 58}, # GEMS_EXP 100
			{"type": "chest", "id": 59}, # MEDICAL_HERB
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_RIGHT_TOWER"},
            {"type": "item", "name": "VIP_CARD"},
        ],
        "act": 6,
    },
    37: {
        "detail": "Region 37 - Act 7 start, World of Evil",
        "description": "World of Evil",
        "checks": [ 
			{"type": "item", "name": "ITEM_KING_MAGRIDD"}, 
			{"type": "chest", "id": 60}, # MEDICAL_HERB
			{"type": "chest", "id": 61}, # GEMS_EXP 200
			{"type": "chest", "id": 62}, #"name": "CHEST_RED_HOT_BALL"}, 
			{"type": "chest", "id": 63}, #"name": "CHEST_SOUL_ARMOR"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_KING_MAGRIDD"},
            {"type": "npc_id", "name": "NPC_SOLDIER_CASTLE"},
            {"type": "item", "name": "BROWN_STONE"},
            {"type": "item", "name": "GREEN_STONE"},
            {"type": "item", "name": "BLUE_STONE"},
            {"type": "item", "name": "SILVER_STONE"},
            {"type": "item", "name": "PURPLE_STONE"},
            {"type": "item", "name": "BLACK_STONE"},
        ],
        "act": 7,
        "is_act_hub": True,
        "connected_regions": [39, 41]
    },
    38: {
        "detail": "Region 38 - Dr Leo + Queen Magridd cutscene",
        "description": "Magridd Castle",
        "checks": [ 
			{"type": "item", "name": "ITEM_DR_LEO"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_WITH_LEO"},
            {"type": "npc_id", "name": "NPC_SOLDIER_DOK"},
            {"type": "npc_id", "name": "NPC_DR_LEO"},
        ],
        "act": 6,
    },
    39: {
        "detail": "Region 39 - Dazzling Space",
        "description": "World of Evil",
        "checks": [ 
			{"type": "chest", "id": 64}, #"name": "CHEST_SOUL_BLADE"}, 
			{"type": "chest", "id": 65}, # GEMS_EXP 100
        ],
        "requirements": [ 
            {"type": "item", "name": "SOUL_ARMOR"},
        ],
        "act": 7,
    },
    40: {
        "detail": "Region 40 - Last Lair in Lune",
        "description": "Lune",
        "checks": [ 
			{"type": "lair", "name": "NPC_SNAIL_EMBLEM_E"}, 
			{"type": "item", "name": "ITEM_EMBLEM_F"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MUSHROOM2"},
            {"type": "npc_id", "name": "NPC_GRANDPA5"},
            {"type": "npc_id", "name": "NPC_MUSHROOM_EMBLEM_F"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 4,
    },
    41: {
        "detail": "Region 41 - End of the game",
        "description": "End of the line...",
        "checks": [ # No checks, but this area needs to be accessible.
        ],
        "requirements": [ 
            {"type": "item", "name": "SOUL_BLADE"},
            {"type": "item", "name": "SOUL_ARMOR"},
            {"type": "item", "name": "PHOENIX"},
        ],
        "act": 7,
        "is_end_region": True
    },
    42: {
        "detail": "Region 42 - Tool Shop Owner",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_TOOL_SHOP_OWNER"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_TOOL_SHOP_OWNER"},
        ],
        "act": 1
    },
    43: {
        "detail": "Region 43 - Tool Shop Owner's son Teddy",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_TEDDY"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_TEDDY"},
        ],
        "act": 1
    },
    44: {
        "detail": "Region 44 - Emblem A tile",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_EMBLEM_A"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_WATER_MILL"},
            {"type": "npc_id", "name": "NPC_IVY"},
            {"type": "npc_id", "name": "NPC_IVY_EMBLEM_A"},
        ],
        "act": 1
    },
    45: {
        "detail": "Region 45 - Secret Cave pass",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_PASS"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_IVY"},
            {"type": "npc_id", "name": "NPC_TULIP_PASS"},
        ],
        "act": 1
    },
    46: {
        "detail": "Region 46 - Goat pen corner tile",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_GOAT_PEN"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_GOAT_HERB"},
        ],
        "act": 1
    },
    47: {
        "detail": "Region 47 - Secret Cave",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_SECRET_CAVE_TILE"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_BOY_CAVE"},
            {"type": "item", "name": "PASS"},
        ],
        "act": 1
    },
    # 
    48: {
        "detail": "Region 48 - Recovery Sword crystal",
        "description": "Grass Valley",
        "checks": [
            {"type": "item", "name": "ITEM_CRYSTAL_RECOVERY_SWORD"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BRIDGE_GUARD"},
            {"type": "npc_id", "name": "NPC_BOY_CAVE"},
            {"type": "item", "name": "PASS"},
            {"type": "npc_id", "name": "NPC_IVY_RECOVERY_SWORD"},
        ],
        "act": 1
    },
    49: {
        "detail": "Region 49 - Red-Hot Mirror bird",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_BIRD_RED_HOT_MIRROR"}
        ],
        "requirements": [ 
            {"type": "item", "name": "RED_HOT_MIRROR"},
        ],
        "act": 2
    },
    50: {
        "detail": "Region 50 - Magic Bell crystal",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_CRYSTAL_MAGIC_BELL"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_DEER_MAGIC_BELL"},
            {"type": "npc_id", "name": "NPC_CROCODILE3"},
            {"type": "item", "name": "EMBLEM_A"},
            {"type": "item", "name": "EMBLEM_B"},
            {"type": "item", "name": "EMBLEM_C"},
            {"type": "item", "name": "EMBLEM_D"},
            {"type": "item", "name": "EMBLEM_E"},
            {"type": "item", "name": "EMBLEM_F"},
            {"type": "item", "name": "EMBLEM_G"},
            {"type": "item", "name": "EMBLEM_H"},
        ],
        "act": 2
    },
    51: {
        "detail": "Region 51 - Woodstin Trio",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_WOODSTIN_TRIO"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_DEER"},
            {"type": "npc_id", "name": "NPC_SQUIRREL3"},
            {"type": "npc_id", "name": "NPC_DOG3"},
        ],
        "act": 2
    },
    52: {
        "detail": "Region 52 - Shield Bracelet mole",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_MOLE_SHIELD_BRACELET"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MOLE"},
            {"type": "npc_id", "name": "NPC_MOLE_SHIELD_BRACELET"},
            {"type": "item", "name": "MOLES_RIBBON"},
        ],
        "act": 2
    },
    53: {
        "detail": "Region 53 - Psycho Sword squirrel",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_SQUIRREL_PSYCHO_SWORD"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SQUIRREL_PSYCHO_SWORD"},
            {"type": "item", "name": "DELICIOUS_SEEDS"},
        ],
        "act": 2
    },
    54: {
        "detail": "Region 54 - Emblem C squirrel",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_SQUIRREL_EMBLEM_C"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SQUIRREL_PSYCHO_SWORD"},
            {"type": "npc_id", "name": "NPC_SQUIRREL_EMBLEM_C"},
        ],
        "act": 2
    },
    55: {
        "description": "St Elles",
        "detail": "Region 55 - Medical Herb mermaid (north-eastern house of St Elles)",
        "checks": [
            {"type": "item", "name": "ITEM_MERMAID_HERB"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_DOLPHIN2"},
            {"type": "npc_id", "name": "NPC_MERMAID"},
        ],
        "act": 3
    },
    56: {
        "detail": "Region 56 - Common Mermaid house",
        "description": "St Elles",
        "checks": [
            {"type": "chest", "id": 22}, # MERMAIDS_TEARS /* WARNING: I hope this chest is safe */
            {"type": "item", "name": "ITEM_MERMAID_BUBBLE_ARMOR"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
        ],
        "act": 3
    },
    57: {
        "detail": "Region 57 - Magic Flare mermaid",
        "description": "St Elles",
        "checks": [
            {"type": "item", "name": "ITEM_MERMAID_MAGIC_FLARE"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_MAGIC_FLARE"},
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
        ],
        "act": 3
    },
    58: {
        "description": "St Elles",
        "detail": "Region 58 - Red-Hot Stick mermaid",
        "checks": [
            {"type": "item", "name": "ITEM_MERMAID_RED_HOT_STICK"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_RED_HOT_STICK"},
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
        ],
        "act": 3
    },
    59: {
        "description": "St Elles",
        "detail": "Region 59 - Lue",
        "checks": [
            {"type": "item", "name": "ITEM_LUE"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_PEARL"},
            {"type": "npc_id", "name": "NPC_LUE"},
            {"type": "npc_id", "name": "NPC_DOLPHIN_SAVES_LUE"},
        ],
        "act": 3
    },
    60: {
        "detail": "Region 60 - Emblem E snail",
        "description": "Mountain of Souls",
        "checks": [
            {"type": "item", "name": "ITEM_SNAIL_EMBLEM_E"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SNAIL_EMBLEM_E"},
        ],
        "act": 4
    },
    61: {
        "description": "Mountain of Souls",
        "detail": "Region 61 - Mushroom Shoes boy",
        "checks": [
            {"type": "item", "name": "ITEM_BOY_MUSHROOM_SHOES"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BOY_MUSHROOM_SHOES"},
        ],
        "act": 4
    },
    62: {
        "detail": "Region 62 - Mountain King's item + Deathtoll appears!",
        "description": "Mountain of Souls",
        "checks": [
            {"type": "item", "name": "ITEM_MOUNTAIN_KING"}
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_BOY_MUSHROOM_SHOES"},
            {"type": "npc_id", "name": "NPC_BOY"},
            {"type": "npc_id", "name": "NPC_GRANDPA3"},
            {"type": "npc_id", "name": "NPC_DANCING_GRANDMA"},
            {"type": "npc_id", "name": "NPC_DANCING_GRANDMA2"},
            {"type": "npc_id", "name": "NPC_MOUNTAIN_KING"},
            {"type": "item", "name": "RED_HOT_BALL"},
            {"type": "item", "name": "RED_HOT_MIRROR"},
            {"type": "item", "name": "RED_HOT_STICK"},
        ],
        "act": 4
    },
    63: {
        "detail": "Region 63 - Locked dining room",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_CHEST_OF_DRAWERS_MYSTIC_ARMOR"},
            {"type": "item", "name": "ITEM_EMBLEM_G"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREAT_DOOR"},
            {"type": "npc_id", "name": "NPC_CHEST_OF_DRAWERS_MYSTIC_ARMOR"},
            {"type": "item", "name": "DOOR_KEY"},
        ],
        "act": 5
    },
    64: {
        "detail": "Region 64 - Spark Magic mouse",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_MOUSE_SPARK_BOMB"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREAT_DOOR"},
            {"type": "npc_id", "name": "NPC_CAT"},
            {"type": "npc_id", "name": "NPC_CAT2"},
            {"type": "npc_id", "name": "NPC_MOUSE"},
            {"type": "npc_id", "name": "NPC_MOUSE_SPARK_BOMB"},
            {"type": "item", "name": "ACTINIDIA_LEAF"},
        ],
        "act": 5
    },
    65: {
        "detail": "Region 65 - Medical Herb plant",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_PLANT_HERB"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREAT_DOOR"},
            {"type": "npc_id", "name": "NPC_CAT"},
            {"type": "npc_id", "name": "NPC_CAT2"},
            {"type": "npc_id", "name": "NPC_MOUSE"},
            {"type": "npc_id", "name": "NPC_PLANT_HERB"},
            {"type": "item", "name": "ACTINIDIA_LEAF"},
        ],
        "act": 5
    },
	66: { # Split from 27 to allow for separate ice armor requirements
        "detail": "Region 66 - Leo's Lab Basement 2",
        "description": "Lab Basement",
        "checks": [ 
			{"type": "lair", "name": "NPC_CAT_DOOR_KEY"}, 
			{"type": "lair", "name": "NPC_STEPS_UPSTAIRS"}, 
			{"type": "lair", "name": "NPC_MOUSE"}, 
			{"type": "lair", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"}, 
			{"type": "lair", "name": "NPC_MODEL_TOWN1"}, 
			{"type": "item", "name": "ITEM_CRYSTAL_LEOS_LAB_BASEMENT"}, 
        ],
        "requirements": [ 
            {"type": "flag", "name": "can_cut_metal"},
       ],
        "act": 5,
    },
    67: {
        "detail": "Region 67 - Leo's Cat",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_CAT_DOOR_KEY"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_CAT_DOOR_KEY"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 5
    },
    68: {
        "detail": "Region 68 - Actinidia Plant",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_PLANT_ACTINIDIA_LEAVES"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_PLANT_ACTINIDIA_LEAVES"},
        ],
        "act": 5
    },
    69: {
        "detail": "Region 69 - Elemental Mail soldier",
        "description": "Magridd Castle",
        "checks": [
            {"type": "item", "name": "ITEM_SOLDIER_ELEMENTAL_MAIL"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_ELEMENTAL_MAIL"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 6
    },
    # WARNING: this item can be lost if the Queen is already dead
    70: {
        "detail": "Region 70 - Queen Magridd",
        "checks": [
            {"type": "item", "name": "ITEM_QUEEN_MAGRIDD"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_QUEEN_MAGRIDD"},
            {"type": "item", "name": "Not an item..."} # Make it impossible to require this item.
        ],
        "act": 6
    },
    71: {
        "detail": "Region 71 - Platinum Card soldier",
        "description": "Magridd Castle",
        "checks": [
            {"type": "item", "name": "ITEM_SOLDIER_PLATINUM_CARD"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SINGER_CONCERT_HALL"},
            {"type": "npc_id", "name": "NPC_SOLDIER_PLATINUM_CARD"},
            {"type": "item", "name": "HARP_STRING"},
        ],
        "act": 6
    },
    72: {
        "description": "Magridd Castle",
        "detail": "Region 72 - Medical Herb maid",
        "checks": [
            {"type": "item", "name": "ITEM_MAID_HERB"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MAID_HERB"},
        ],
        "act": 6
    },
    73: {
        "detail": "Region 73 - Magridd Castle + Emblem H tile",
        "description": "Magridd Castle",
        "checks": [
            {"type": "item", "name": "ITEM_EMBLEM_H"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_CASTLE"},
        ],
        "act": 6
    },
    74: {
        "detail": "Region 74 - Super Bracelet tile",
        "description": "Magridd Castle",
        "checks": [
            {"type": "item", "name": "ITEM_SUPER_BRACELET"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_QUEEN_MAGRIDD"},
            {"type": "npc_id", "name": "NPC_SOLDIER_WITH_LEO"},
            {"type": "npc_id", "name": "NPC_SOLDIER_DOK"},
            {"type": "npc_id", "name": "NPC_DR_LEO"},
        ],
        "act": 6
    },
    75: {
        "detail": "Region 75 - Greenwood Leaf tile",
        "description": "Greenwood",
        "checks": [
            {"type": "item", "name": "ITEM_GREENWOOD_LEAVES"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_CROCODILE"},
            {"type": "npc_id", "name": "NPC_CROCODILE2"},
            {"type": "npc_id", "name": "NPC_BIRD_GREENWOOD_LEAF"},
            {"type": "npc_id", "name": "NPC_MOLE_SOUL_OF_LIGHT"},
            {"type": "item", "name": "DREAM_ROD"},
        ],
        "act": 6
    },
    76: {
        "detail": "Region 76 - Demon Bird's lair",
        "description": "Magridd Castle",
        "checks": [
            {"type": "lair", "name": "NPC_KING_MAGRIDD"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_SOLDIER_RIGHT_TOWER"},
            {"type": "item", "name": "VIP_CARD"},
            {"type": "item", "name": "MOBILE_KEY"},
        ],
        "act": 6
    },
	77: { # Split from 18 to allow for mermaid's tears requirement
        "detail": "Region 77 - Durean",
        "description": "Durean",
        "checks": [ 
			# {"type": "lair", "name": "NPC_DOLPHIN_PEARL"}, 
			# {"type": "lair", "name": "NPC_LUE"}, 
			{"type": "lair", "name": "NPC_MERMAID_PEARL"}, 
			# {"type": "lair", "name": "NPC_MERMAID2"}, 
			# {"type": "lair", "name": "NPC_MERMAID_NANA"}, 
			# {"type": "lair", "name": "NPC_DOLPHIN_SAVES_LUE"}, 
			# {"type": "lair", "name": "NPC_MERMAID3"}, 
			{"type": "lair", "name": "NPC_MERMAID_STATUE_BLESTER"}, 
			{"type": "chest", "id": 31}, # CRITICAL_SWORD
			# {"type": "chest", "id": 32}, # STRANGE_BOTTLE
			# {"type": "item", "name": "ITEM_CRYSTAL_SEABED_NEAR_DUREAN"}, 
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_MERMAID_STATUE_DUREAN"}, 
            {"type": "npc_id", "name": "NPC_MERMAID_BUBBLE_ARMOR"},
            # {"type": "item", "name": "MERMAIDS_TEARS"}, # Opted not to make this required.
       ],
        "act": 3
    },
    78: {
        "detail": "Region 78 - Chest of Drawers in Attic",
        "description": "Leo`s Lab",
        "checks": [
            {"type": "item", "name": "ITEM_CHEST_OF_DRAWERS_HERB"},
        ],
        "requirements": [ 
            {"type": "npc_id", "name": "NPC_GREAT_DOOR_MODEL_TOWNS"},
            {"type": "npc_id", "name": "NPC_STEPS_UPSTAIRS"},
            {"type": "npc_id", "name": "NPC_STEPS_MARIE"},
            {"type": "npc_id", "name": "NPC_CHEST_OF_DRAWERS2"},
        ],
        "act": 6
    },
}

NON_KEY_NPCS = [ 
    "NPC_TULIP",
    "NPC_TULIP2",
    "NPC_GOAT",
    "NPC_TULIP3",
    "NPC_LONELY_GOAT",
    "NPC_BOY_CABIN",
    "NPC_OLD_MAN",
    "NPC_OLD_MAN2",
    "NPC_IVY2",
    "NPC_TULIP4",
    "NPC_GOAT2",
    "NPC_BIRD",
    "NPC_DOG",
    "NPC_DOG2",
    "NPC_BIRD2",
    "NPC_SQUIRREL",
    "NPC_DOG4",
    "NPC_SQUIRREL2",
    "NPC_DOG5",
    "NPC_MOLE2",
    "NPC_BIRD3",
    "NPC_DOLPHIN",
    "NPC_ANGELFISH",
    "NPC_ANGELFISH2",
    "NPC_MERMAID2",
    "NPC_MERMAID3",
    "NPC_MERMAID_NANA",
    "NPC_MERMAID4",
    "NPC_MERMAID5",
    "NPC_MERMAID6",
    "NPC_MERMAID_TEARS",
    "NPC_ANGELFISH3",
    "NPC_ANGELFISH_SOUL_OF_SHIELD",
    "NPC_MERMAID7",
    "NPC_ANGELFISH4",
    "NPC_MERMAID8",
    "NPC_MERMAID9",
    "NPC_GRANDPA",
    "NPC_GIRL",
    "NPC_MUSHROOM",
    "NPC_GRANDPA2",
    "NPC_SNAIL_JOCKEY",
    "NPC_BOY2",
    "NPC_GRANDMA",
    "NPC_GIRL2",
    "NPC_SNAIL_RACER",
    "NPC_SNAIL_RACER2",
    "NPC_MUSHROOM3",
    "NPC_SNAIL",
    "NPC_SNAIL2",
    "NPC_PLANT",
    "NPC_CAT3",
    "NPC_DOLL",
    "NPC_CHEST_OF_DRAWERS",
    "NPC_PLANT2",
    "NPC_MOUSE2",
    "NPC_MOUSE3",
    "NPC_GREAT_DOOR_SOUL_OF_DETECTION",
    "NPC_MOUSE4",
    "NPC_MOUSE5",
    "NPC_CAT4",
    "NPC_SOLDIER",
    "NPC_SOLDIER2",
    "NPC_SOLDIER3",
    "NPC_SOLDIER4",
    "NPC_SOLDIER5",
    "NPC_SOLDIER6",
    "NPC_MAID",
    "NPC_SINGER",
    "NPC_SOLDIER_SOUL_OF_REALITY",
    "NPC_MAID2",
    "NPC_SOLDIER7",
    "NPC_SOLDIER8",
    "NPC_SOLDIER9",
    "NPC_SOLDIER10",
    "NPC_SOLDIER11",
]

NPC_ITEMS = [
	{
		"npc_id": "ITEM_TOOL_SHOP_OWNER",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_EMBLEM_A",
		"item_id": "EMBLEM_A"
	},
	{
		"npc_id": "ITEM_GOAT_PEN",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_TEDDY",
		"item_id": "GOATS_FOOD"
	},
	{
		"npc_id": "ITEM_PASS",
		"item_id": "PASS"
	},
	{
		"npc_id": "ITEM_SECRET_CAVE_TILE",
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"npc_id": "ITEM_VILLAGE_CHIEF",
		"item_id": "BROWN_STONE"
	},
	{
		"npc_id": "ITEM_MAGICIAN",
		"item_id": "FLAME_BALL"
	},
	{
		"npc_id": "ITEM_CRYSTAL_RECOVERY_SWORD",
		"item_id": "RECOVERY_SWORD"
	},
	{
		"npc_id": "ITEM_BIRD_RED_HOT_MIRROR",
		"item_id": "RED_HOT_MIRROR"
	},
	{
		"npc_id": "ITEM_CRYSTAL_MAGIC_BELL",
		"item_id": "MAGIC_BELL"
	},
	{
		"npc_id": "ITEM_WOODSTIN_TRIO",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_GREENWOODS_GUARDIAN",
		"item_id": "GREEN_STONE"
	},
	{
		"npc_id": "ITEM_GREENWOOD_LEAVES",
		"item_id": "GREENWOOD_LEAF"
	},
	{
		"npc_id": "ITEM_MOLE_SHIELD_BRACELET",
		"item_id": "SHIELD_BRACELET"
	},
	{
		"npc_id": "ITEM_SQUIRREL_PSYCHO_SWORD",
		"item_id": "PSYCHO_SWORD"
	},
	{
		"npc_id": "ITEM_SQUIRREL_EMBLEM_C",
		"item_id": "EMBLEM_C"
	},
	{
		"npc_id": "ITEM_WATER_SHRINE_TILE",
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"npc_id": "ITEM_CRYSTAL_LIGHT_ARROW",
		"item_id": "LIGHT_ARROW"
	},
	{
		"npc_id": "ITEM_MOUNTAIN_KING",
		"item_id": "PHOENIX"
	},
	{
		"npc_id": "ITEM_BOY_MUSHROOM_SHOES",
		"item_id": "MUSHROOM_SHOES"
	},
	{
		"npc_id": "ITEM_NOME",
		"item_id": "SILVER_STONE"
	},
	{
		"npc_id": "ITEM_SNAIL_EMBLEM_E",
		"item_id": "EMBLEM_E"
	},
	{
		"npc_id": "ITEM_EMBLEM_F",
		"item_id": "EMBLEM_F"
	},
	{
		"npc_id": "ITEM_EMBLEM_G",
		"item_id": "EMBLEM_G"
	},
	{
		"npc_id": "ITEM_CHEST_OF_DRAWERS_MYSTIC_ARMOR",
		"item_id": "MYSTIC_ARMOR"
	},
	{
		"npc_id": "ITEM_PLANT_HERB",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_CAT_DOOR_KEY",
		"item_id": "DOOR_KEY"
	},
	{
		"npc_id": "ITEM_PLANT_ACTINIDIA_LEAVES",
		"item_id": "ACTINIDIA_LEAF"
	},
	{
		"npc_id": "ITEM_CHEST_OF_DRAWERS_HERB",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_MARIE",
		"item_id": "PURPLE_STONE"
	},
	{
		"npc_id": "ITEM_MOUSE_SPARK_BOMB",
		"item_id": "SPARK_BOMB"
	},
	{
		"npc_id": "ITEM_SOLDIER_ELEMENTAL_MAIL",
		"item_id": "ELEMENTAL_MAIL"
	},
	{
		"npc_id": "ITEM_SUPER_BRACELET",
		"item_id": "SUPER_BRACELET"
	},
	{
		"npc_id": "ITEM_QUEEN_MAGRIDD",
		"item_id": "VIP_CARD"
	},
	{
		"npc_id": "ITEM_SOLDIER_PLATINUM_CARD",
		"item_id": "PLATINUM_CARD"
	},
	{
		"npc_id": "ITEM_MAID_HERB",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_EMBLEM_H",
		"item_id": "EMBLEM_H"
	},
	{
		"npc_id": "ITEM_KING_MAGRIDD",
		"item_id": "BLACK_STONE"
	},
	{
		"npc_id": "ITEM_DR_LEO",
		"item_id": "MOBILE_KEY"
	},
	{
		"npc_id": "ITEM_HARP_STRING",
		"item_id": "HARP_STRING"
	},
	{
		"npc_id": "ITEM_MERMAID_HERB",
		"item_id": "MEDICAL_HERB"
	},
	{
		"npc_id": "ITEM_MERMAID_BUBBLE_ARMOR",
		"item_id": "BUBBLE_ARMOR"
	},
	{
		"npc_id": "ITEM_MERMAID_MAGIC_FLARE",
		"item_id": "MAGIC_FLARE"
	},
	{
		"npc_id": "ITEM_MERMAID_QUEEN",
		"item_id": "BLUE_STONE"
	},
	{
		"npc_id": "ITEM_MERMAID_RED_HOT_STICK",
		"item_id": "RED_HOT_STICK"
	},
	{
		"npc_id": "ITEM_LUE",
		"item_id": "THUNDER_RING"
	},
	{
		"npc_id": "ITEM_CRYSTAL_GRASS_VALLEY",
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"npc_id": "ITEM_CRYSTAL_UNDERGROUND_CASTLE",
		"item_id": "GEMS_EXP",
		"amount": 30
	},
	{
		"npc_id": "ITEM_CRYSTAL_LOST_MARSH",
		"item_id": "GEMS_EXP",
		"amount": 150
	},
	{
		"npc_id": "ITEM_CRYSTAL_WATER_SHRINE",
		"item_id": "GEMS_EXP",
		"amount": 180
	},
	{
		"npc_id": "ITEM_CRYSTAL_FIRE_SHRINE",
		"item_id": "GEMS_EXP",
		"amount": 1
	},
	{
		"npc_id": "ITEM_CRYSTAL_MOUNTAIN_OF_SOULS",
		"item_id": "GEMS_EXP",
		"amount": 300
	},
	{
		"npc_id": "ITEM_CRYSTAL_LUNE",
		"item_id": "GEMS_EXP",
		"amount": 400
	},
	{
		"npc_id": "ITEM_CRYSTAL_LEOS_LAB_BASEMENT",
		"item_id": "GEMS_EXP",
		"amount": 300
	},
	{
		"npc_id": "ITEM_CRYSTAL_MODEL_TOWN",
		"item_id": "GEMS_EXP",
		"amount": 300
	},
	{
		"npc_id": "ITEM_CRYSTAL_POWER_PLANT",
		"item_id": "GEMS_EXP",
		"amount": 300
	},
	{
		"npc_id": "ITEM_CRYSTAL_ROCKBIRD",
		"item_id": "GEMS_EXP",
		"amount": 200
	},
	{
		"npc_id": "ITEM_CRYSTAL_SEABED_NEAR_BLESTER",
		"item_id": "GEMS_EXP",
		"amount": 300
	},
	{
		"npc_id": "ITEM_CRYSTAL_SEABED_NEAR_DUREAN",
		"item_id": "GEMS_EXP",
		"amount": 250
	}
]

# List of chest contents:
# 
#      - Medical Herb x13         - Mole's Ribbon
#      - Strange Bottle x5        - Big Pearl
#      - Sword of Life            - Mermaid's Tears
#      - Critical Sword           - Delicious Seeds
#      - Lucky Blade              - Emblem B
#      - Zantetsu Sword           - Emblem D
#      - Spirit Sword             - Red-Hot Ball
#      - Soul Blade               - Power Bracelet
#      - Iron Armor               - 1 Gem
#      - Ice Armor                - 12 Gems
#      - Magic Armor              - 40 Gems
#      - Light Armor              - 50 Gems x5
#      - Soul Armor               - 60 Gems x2
#      - Rotator                  - 80 Gems x5
#      - Flame Pillar             - 100 Gems x4
#      - Tornado                  - 150 Gems
#      - Dream Rod                - 200 Gems
#      - Leo's Brush              - Nothing x3
# 
#     Total: 66 chests

CHEST_ITEMS = [
	{
		"chest_id": 0,
		"item_id": "SWORD_OF_LIFE"
	},
	{
		"chest_id": 1,
		"item_id": "IRON_ARMOR"
	},
	{
		"chest_id": 2,
		"item_id": "GEMS_EXP",
		"amount": 50
	},
	{
		"chest_id": 3,
		"item_id": "GEMS_EXP",
		"amount": 12
	},
	{
		"chest_id": 4,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 5,
		"item_id": "DREAM_ROD"
	},
	{
		"chest_id": 6,
		"item_id": "LEOS_BRUSH"
	},
	{
		"chest_id": 7,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 8,
		"item_id": "TORNADO"
	},
	{
		"chest_id": 9,
		"item_id": "ICE_ARMOR"
	},
	{
		"chest_id": 10,
		"item_id": "MOLES_RIBBON"
	},
	{
		"chest_id": 11,
		"item_id": "GEMS_EXP",
		"amount": 50
	},
	{
		"chest_id": 12,
		"item_id": "GEMS_EXP",
		"amount": 150
	},
	{
		"chest_id": 13,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 14,
		"item_id": "DELICIOUS_SEEDS"
	},
	{
		"chest_id": 15,
		"item_id": "GEMS_EXP",
		"amount": 50
	},
	{
		"chest_id": 16,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 17,
		"item_id": "NOTHING"
	},
	{
		"chest_id": 18,
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"chest_id": 19,
		"item_id": "GEMS_EXP",
		"amount": 100
	},
	{
		"chest_id": 20,
		"item_id": "GEMS_EXP",
		"amount": 60
	},
	{
		"chest_id": 21,
		"item_id": "FLAME_PILLAR"
	},
	{
		"chest_id": 22,
		"item_id": "MERMAIDS_TEARS"
	},
	{
		"chest_id": 23,
		"item_id": "BIG_PEARL"
	},
	{
		"chest_id": 24,
		"item_id": "EMBLEM_D"
	},
	{
		"chest_id": 25,
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"chest_id": 26,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 27,
		"item_id": "NOTHING"
	},
	{
		"chest_id": 28,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 29,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 30,
		"item_id": "GEMS_EXP",
		"amount": 60
	},
	{
		"chest_id": 31,
		"item_id": "CRITICAL_SWORD"
	},
	{
		"chest_id": 32,
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"chest_id": 33,
		"item_id": "GEMS_EXP",
		"amount": 1
	},
	{
		"chest_id": 34,
		"item_id": "POWER_BRACELET"
	},
	{
		"chest_id": 35,
		"item_id": "GEMS_EXP",
		"amount": 40
	},
	{
		"chest_id": 36,
		"item_id": "MAGIC_ARMOR"
	},
	{
		"chest_id": 37,
		"item_id": "NOTHING"
	},
	{
		"chest_id": 38,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 39,
		"item_id": "GEMS_EXP",
		"amount": 50
	},
	{
		"chest_id": 40,
		"item_id": "LUCKY_BLADE"
	},
	{
		"chest_id": 41,
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"chest_id": 42,
		"item_id": "ROTATOR"
	},
	{
		"chest_id": 43,
		"item_id": "ZANTETSU_SWORD"
	},
	{
		"chest_id": 44,
		"item_id": "LIGHT_ARMOR"
	},
	{
		"chest_id": 45,
		"item_id": "GEMS_EXP",
		"amount": 50
	},
	{
		"chest_id": 46,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 47,
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"chest_id": 48,
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"chest_id": 49,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 50,
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"chest_id": 51,
		"item_id": "SPIRIT_SWORD"
	},
	{
		"chest_id": 52,
		"item_id": "STRANGE_BOTTLE"
	},
	{
		"chest_id": 53,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 54,
		"item_id": "GEMS_EXP",
		"amount": 100
	},
	{
		"chest_id": 55,
		"item_id": "EMBLEM_B"
	},
	{
		"chest_id": 56,
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"chest_id": 57,
		"item_id": "GEMS_EXP",
		"amount": 80
	},
	{
		"chest_id": 58,
		"item_id": "GEMS_EXP",
		"amount": 100
	},
	{
		"chest_id": 59,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 60,
		"item_id": "MEDICAL_HERB"
	},
	{
		"chest_id": 61,
		"item_id": "GEMS_EXP",
		"amount": 200
	},
	{
		"chest_id": 62,
		"item_id": "RED_HOT_BALL"
	},
	{
		"chest_id": 63,
		"item_id": "SOUL_ARMOR"
	},
	{
		"chest_id": 64,
		"item_id": "SOUL_BLADE"
	},
	{
		"chest_id": 65,
		"item_id": "GEMS_EXP",
		"amount": 100
	}
]
