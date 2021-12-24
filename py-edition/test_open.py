import os, pickle

print(__file__)

script_dir = os.path.dirname(__file__)
rom_name = 'Soul Blazer (U) [!].smc'


print(script_dir)

rom_location = os.path.join(script_dir, rom_name)

print(rom_location)

with open(rom_location, 'rb') as f:
    # Do file operations...
    rom_content = pickle.load(f)

# print(type(rom_content))
print(str(rom_content)[0, 200])

