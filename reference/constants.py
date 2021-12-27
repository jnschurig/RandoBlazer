import os 

REFERENCE_DIR = os.path.dirname(__file__)
REPOSITORY_ROOT_DIR = os.path.abspath(os.path.join(REFERENCE_DIR, '..'))
version_file = os.path.join(REPOSITORY_ROOT_DIR, 'version.txt')

with open(version_file, 'r') as f:
    VERSION_CODE = f.read()
