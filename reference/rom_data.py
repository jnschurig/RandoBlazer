
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
