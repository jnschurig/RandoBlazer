import os

print('Check pip version and update...')
os.system('python -m pip install --upgrade pip')
# print(pip_upgrade_cmd)

try:
    import networkx 
    print('Found package networkx')
except:
    print('networkx package not found. Attempting to install...')
    try:
        os.system('pip install networkx')
    except:
        print('Unable to install dependency.')
