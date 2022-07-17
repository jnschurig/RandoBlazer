import os 

REFERENCE_DIR = os.path.dirname(__file__)
REPOSITORY_ROOT_DIR = os.path.abspath(os.path.join(REFERENCE_DIR, '..'))

with open(os.path.join(REPOSITORY_ROOT_DIR, 'version.txt'), 'r') as f:
    VERSION_CODE = f.read()

SEED_MIN = 1000000000
SEED_MAX = 3656158440062975 # zzzzzzzzzz in base 36

DEFAULT_RANDOM_MAX_INT = 100

# NUMBER_OF_CHESTS  = 66
# NUMBER_OF_ITEMS   = 126
NUMBER_OF_LAIRS   = 420 # Blaze it
NUMBER_OF_SPRITES = 205

CHEST_DATA_ADDRESS = 0xAADE
MONSTER_LAIR_DATA_ADDRESS = 0xBA0D

ROM_HASH_MD5_UNHEADERED = '83cf41d53a1b94aeea1a645037a24004'
ROM_HASH_MD5_HEADERED = 'baa6aae1e8624650e3e56a9e57594a29'

SEED_BASE = 36

MAX_LOOPS = 20

RANDOM_GEM_LIMIT = [2, 500] # 2 is the minimum because we already have 1

DEFAULT_TRASH_WEIGHTS = {
	'MEDICAL_HERB': 12,
	'STRANGE_BOTTLE': 4,
	'NOTHING': 2,
	'GEMS_EXP': 20
}

BASE_LOOKUP = {
	0 : '0',
	1 : '1',
	2 : '2',
	3 : '3',
	4 : '4',
	5 : '5',
	6 : '6',
	7 : '7',
	8 : '8',
	9 : '9',
	10: 'a',
	11: 'b',
	12: 'c',
	13: 'd',
	14: 'e',
	15: 'f',
	16: 'g',
	17: 'h',
	18: 'i',
	19: 'j',
	20: 'k',
	21: 'l',
	22: 'm',
	23: 'n',
	24: 'o',
	25: 'p',
	26: 'q',
	27: 'r',
	28: 's',
	29: 't',
	30: 'u',
	31: 'v',
	32: 'w',
	33: 'x',
	34: 'y',
	35: 'z'
}

VALID_WORLD_TYPES = ['vanilla', 'balanced', 'advanced']

VALID_TRASH_SETTINGS = ['vanilla', 'random', '<ITEM>', 'none']

DEFAULT_RANDO_SETTINGS = {
    'world_type': 'balanced',
    'starting_weapon': 'RANDOM',
    'magician_item': 'RANDOM',
}

TRASH_FILL_METHODS = ['vanilla', 'equilized', '<ITEMs>']

VANILLA_TRASH_WEIGHTS = {
	'MEDICAL_HERB': 19,
	'STRANGE_BOTTLE': 7,
	'GEM_EXP': 33,
	'NOTHING': 3,
}
