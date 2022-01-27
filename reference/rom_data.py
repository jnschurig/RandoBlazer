
SPRITE_ADDRESSES = {
    "act1": [
        0x9CCA, 0x9CCE, 0x9CD2, 0x9CD6, 0x9CDA, 0x9CDE, 0x9CE2, 0x9CE6, 0x9CEA, 0x9CEE,
        0x9CF2, 0x9D1B, 0x9D1F, 0x9D23, 0x9D27, 0x9D2B, 0x9D2F, 0x9D33, 0x9D37, 0x9D3B,
        0x9D3F, 0x9D43, 0x9D47, 0x9D4B, 0x9D4F, 0x9D53, 0x9D57
    ],
    "act2": [ 
        0x9F01, 0x9F05, 0x9F09, 0x9F0D, 0x9F11, 0x9F15, 0x9F19, 0x9F1D, 0x9F21, 0x9F25,
        0x9F29, 0x9F2D, 0x9F31, 0x9F35, 0x9F6A, 0x9F6E, 0x9F72, 0x9F76, 0x9F93, 0x9F97,
        0x9F9B, 0x9F9F, 0x9FA3, 0x9FA7, 0x9FAB
    ],
    "act3": [
        0xA11C, 0xA120, 0xA124, 0xA128, 0xA12C, 0xA130, 0xA194, 0xA198, 0xA19C, 0xA1A0,
        0xA1A4, 0xA1A8, 0xA1AC, 0xA1B0, 0xA1B4, 0xA1B8, 0xA1D1, 0xA1D5, 0xA1D9, 0xA1DD,
        0xA1E1, 0xA1E5, 0xA1E9, 0xA1ED, 0xA202, 0xA206, 0xA20A, 0xA20E, 0xA212, 0xA243,
        0xA247, 0xA24B, 0xA24F, 0xA253, 0xA28C, 0xA290, 0xA294, 0xA298
    ],
    "act4": [
        0xA3B9, 0xA3BD, 0xA3C1, 0xA3C5, 0xA3C9, 0xA407, 0xA40B, 0xA40F, 0xA413, 0xA42C,
        0xA430, 0xA434, 0xA438, 0xA47B, 0xA47F, 0xA498, 0xA49C, 0xA4A0, 0xA4A4, 0xA4C5,
        0xA4C9, 0xA4CD, 0xA4D1, 0xA4D5, 0xA4D9, 0xA4DD, 0xA4E1
    ],
    "act5": [
        0xA608, 0xA60C, 0xA610, 0xA614, 0xA618, 0xA61C, 0xA63D, 0xA641, 0xA645, 0xA649,
        0xA64D, 0xA651
    ],
    "act6": [
        0xA6CB, 0xA6CF, 0xA6D3, 0xA6D7, 0xA6DB, 0xA6DF, 0xA6E3, 0xA6E7, 0xA6EB, 0xA6EF,
        0xA6F3, 0xA708, 0xA70C, 0xA710, 0xA714, 0xA718, 0xA71C, 0xA751, 0xA755, 0xA759,
        0xA75D, 0xA761, 0xA765, 0xA77F, 0xA783, 0xA787, 0xA78B, 0xA78F, 0xA793, 0xA797,
        0xA79B, 0xA79F, 0xA7A3, 0xA7A7, 0xA7AB, 0xA7BC, 0xA7C0, 0xA7C4, 0xA7C8, 0xA7CC,
        0xA7D0, 0xA7D4, 0xA7D8, 0xA7F6, 0xA7FA, 0xA7FE, 0xA802, 0xA806, 0xA80A, 0xA81B,
        0xA81F, 0xA823, 0xA827, 0xA834, 0xA838, 0xA83C, 0xA840, 0xA844, 0xA848, 0xA84C,
        0xA850, 0xA861, 0xA865
    ],
    "act7": [
        0xA946, 0xA94A, 0xA94E, 0xA952, 0xA956, 0xA95A, 0xA95E, #0xA987, 0xA98B, 0xA98F, 
        0xA993, 0xA997, 0xA99B, 0xA99F, 0xA9A3, 0xA9A7 # Three bricks for grinding ^^.
    ]
}

ITEMS = {
    "NOTHING"        : {"rom_value": b'\x00', "pretty_name": "Nothing"},
    "SWORD_OF_LIFE"  : {"rom_value": b'\x01', "pretty_name": "Sword of Life"},
    "PSYCHO_SWORD"   : {"rom_value": b'\x02', "pretty_name": "Psycho Sword"},
    "CRITICAL_SWORD" : {"rom_value": b'\x03', "pretty_name": "Critical Sword"},
    "LUCKY_BLADE"    : {"rom_value": b'\x04', "pretty_name": "Lucky Blade"},
    "ZANTETSU_SWORD" : {"rom_value": b'\x05', "pretty_name": "Zantetsu Sword"},
    "SPIRIT_SWORD"   : {"rom_value": b'\x06', "pretty_name": "Spirit Sword"},
    "RECOVERY_SWORD" : {"rom_value": b'\x07', "pretty_name": "Recovery Sword"},
    "SOUL_BLADE"     : {"rom_value": b'\x08', "pretty_name": "Soul Blade"},
    "IRON_ARMOR"     : {"rom_value": b'\x09', "pretty_name": "Iron Armor"},
    "ICE_ARMOR"      : {"rom_value": b'\x0A', "pretty_name": "Ice Armor"},
    "BUBBLE_ARMOR"   : {"rom_value": b'\x0B', "pretty_name": "Bubble Armor"},
    "MAGIC_ARMOR"    : {"rom_value": b'\x0C', "pretty_name": "Magic Armor"},
    "MYSTIC_ARMOR"   : {"rom_value": b'\x0D', "pretty_name": "Mystic Armor"},
    "LIGHT_ARMOR"    : {"rom_value": b'\x0E', "pretty_name": "Light Armor"},
    "ELEMENTAL_MAIL" : {"rom_value": b'\x0F', "pretty_name": "Elemental Mail"},
    "SOUL_ARMOR"     : {"rom_value": b'\x10', "pretty_name": "Soul Armor"},
    "FLAME_BALL"     : {"rom_value": b'\x11', "pretty_name": "Flame Ball"},
    "LIGHT_ARROW"    : {"rom_value": b'\x12', "pretty_name": "Light Arrow"},
    "MAGIC_FLARE"    : {"rom_value": b'\x13', "pretty_name": "Magic Flare"},
    "ROTATOR"        : {"rom_value": b'\x14', "pretty_name": "Rotator"},
    "SPARK_BOMB"     : {"rom_value": b'\x15', "pretty_name": "Spark Bomb"},
    "FLAME_PILLAR"   : {"rom_value": b'\x16', "pretty_name": "Flame Pillar"},
    "TORNADO"        : {"rom_value": b'\x17', "pretty_name": "Tornado"},
    "PHOENIX"        : {"rom_value": b'\x18', "pretty_name": "Phoenix"},
    "GOATS_FOOD"     : {"rom_value": b'\x19', "pretty_name": "Goat`s Food"},
    "HARP_STRING"    : {"rom_value": b'\x1A', "pretty_name": "Harp String"},
    "PASS"           : {"rom_value": b'\x1B', "pretty_name": "Pass"},
    "DREAM_ROD"      : {"rom_value": b'\x1C', "pretty_name": "Dream Rod"},
    "LEOS_BRUSH"     : {"rom_value": b'\x1D', "pretty_name": "Leo`s Brush"},
    "GREENWOOD_LEAF" : {"rom_value": b'\x1E', "pretty_name": "Greenwood Leaf"},
    "MOLES_RIBBON"   : {"rom_value": b'\x1F', "pretty_name": "Mole`s Ribbon"},
    "BIG_PEARL"      : {"rom_value": b'\x20', "pretty_name": "Big Pearl"},
    "MERMAIDS_TEARS" : {"rom_value": b'\x21', "pretty_name": "Mermaid`s Tears"},
    "MUSHROOM_SHOES" : {"rom_value": b'\x22', "pretty_name": "Mushroom Shoes"},
    "MOBILE_KEY"     : {"rom_value": b'\x23', "pretty_name": "Mobile Key"},
    "THUNDER_RING"   : {"rom_value": b'\x24', "pretty_name": "Thunder Ring"},
    "DELICIOUS_SEEDS": {"rom_value": b'\x25', "pretty_name": "Delicious Seeds"},
    "ACTINIDIA_LEAF" : {"rom_value": b'\x26', "pretty_name": "Actinidia Leaf"},
    "DOOR_KEY"       : {"rom_value": b'\x27', "pretty_name": "Door Key"},
    "PLATINUM_CARD"  : {"rom_value": b'\x28', "pretty_name": "Platinum Card"},
    "VIP_CARD"       : {"rom_value": b'\x29', "pretty_name": "VIP Card"},
    "EMBLEM_A"       : {"rom_value": b'\x2A', "pretty_name": "Emblem A"},
    "EMBLEM_B"       : {"rom_value": b'\x2B', "pretty_name": "Emblem B"},
    "EMBLEM_C"       : {"rom_value": b'\x2C', "pretty_name": "Emblem C"},
    "EMBLEM_D"       : {"rom_value": b'\x2D', "pretty_name": "Emblem D"},
    "EMBLEM_E"       : {"rom_value": b'\x2E', "pretty_name": "Emblem E"},
    "EMBLEM_F"       : {"rom_value": b'\x2F', "pretty_name": "Emblem F"},
    "EMBLEM_G"       : {"rom_value": b'\x30', "pretty_name": "Emblem G"},
    "EMBLEM_H"       : {"rom_value": b'\x31', "pretty_name": "Emblem H"},
    "RED_HOT_MIRROR" : {"rom_value": b'\x32', "pretty_name": "Red-Hot Mirror"},
    "RED_HOT_BALL"   : {"rom_value": b'\x33', "pretty_name": "Red-Hot Ball"},
    "RED_HOT_STICK"  : {"rom_value": b'\x34', "pretty_name": "Red-Hot Stick"},
    "POWER_BRACELET" : {"rom_value": b'\x35', "pretty_name": "Power Bracelet"},
    "SHIELD_BRACELET": {"rom_value": b'\x36', "pretty_name": "Shield Bracelet"},
    "SUPER_BRACELET" : {"rom_value": b'\x37', "pretty_name": "Super Bracelet"},
    "MEDICAL_HERB"   : {"rom_value": b'\x38', "pretty_name": "Medical Herb"},
    "STRANGE_BOTTLE" : {"rom_value": b'\x39', "pretty_name": "Strange Bottle"},
    "BROWN_STONE"    : {"rom_value": b'\x3A', "pretty_name": "Brown Stone"},
    "GREEN_STONE"    : {"rom_value": b'\x3B', "pretty_name": "Green Stone"},
    "BLUE_STONE"     : {"rom_value": b'\x3C', "pretty_name": "Blue Stone"},
    "SILVER_STONE"   : {"rom_value": b'\x3D', "pretty_name": "Silver Stone"},
    "PURPLE_STONE"   : {"rom_value": b'\x3E', "pretty_name": "Purple Stone"},
    "BLACK_STONE"    : {"rom_value": b'\x3F', "pretty_name": "Black Stone"},
    "MAGIC_BELL"     : {"rom_value": b'\x40', "pretty_name": "Magic Bell"},
    "GEMS_EXP"       : {"rom_value": b'\xFF'}
 }


npc_items = [
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

'''    
List of chest contents:

     - Medical Herb x13         - Mole's Ribbon
     - Strange Bottle x5        - Big Pearl
     - Sword of Life            - Mermaid's Tears
     - Critical Sword           - Delicious Seeds
     - Lucky Blade              - Emblem B
     - Zantetsu Sword           - Emblem D
     - Spirit Sword             - Red-Hot Ball
     - Soul Blade               - Power Bracelet
     - Iron Armor               - 1 Gem
     - Ice Armor                - 12 Gems
     - Magic Armor              - 40 Gems
     - Light Armor              - 50 Gems x5
     - Soul Armor               - 60 Gems x2
     - Rotator                  - 80 Gems x5
     - Flame Pillar             - 100 Gems x4
     - Tornado                  - 150 Gems
     - Dream Rod                - 200 Gems
     - Leo's Brush              - Nothing x3

    Total: 66 chests
'''

CHESTS = [
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