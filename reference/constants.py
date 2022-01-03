import os 

REFERENCE_DIR = os.path.dirname(__file__)
REPOSITORY_ROOT_DIR = os.path.abspath(os.path.join(REFERENCE_DIR, '..'))

with open(os.path.join(REPOSITORY_ROOT_DIR, 'version.txt'), 'r') as f:
    VERSION_CODE = f.read()

SEED_MIN = 1000000000
SEED_MAX = 9999999999

DEFAULT_RANDOM_MAX_INT = 100
