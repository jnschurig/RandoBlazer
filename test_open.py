import os, sys, binascii
# from constants import text

# print(__file__)

script_dir = os.path.dirname(__file__)
rom_name = 'Soul Blazer (U) [!].smc'


print(script_dir)

rom_location = os.path.join(script_dir, rom_name)

print(rom_location)

with open(rom_location, 'rb') as f:
    # Do file operations...
    # rom_content = pickle.load(f)
    rom_content = f.read()

# print(rom_content[:50])
# print(str(rom_content)[0, 200])
# print(type(rom_content))

# Seek and write example...

# with file('file.bin', 'r+b') as fh:
#     # apply patch1
#     fh.seek(0xc0010)
#     fh.write(patch1)
#     fh.seek(0x7c0010)
#     fh.write(patch1)
#     # apply patch2
#     fh.seek(0x040000)
#     fh.write(patch2)

# Kind of helpful document for writing memory locations...
# https://stackoverflow.com/questions/14643538/modifying-binary-file-with-python

output_rom_location = os.path.join(script_dir, 'output_rom.smc')

# print(res)
# print(type(res))
# sys.exit('temp breaking point')

print(type(b'hi'))
print(type('hi'))
print(type(1))
print(type(bytearray(1)))
print(type(1.1))
print(type(bytearray(1.1)))
sys.exit(1)


with open(output_rom_location, 'wb') as f:
    f.write(rom_content)
    for filler in text.FILLER_REPLACEMENT:
        f.seek(filler['address'])
        pad_value = ''.ljust(filler['length'], filler['character'])
        pad_value = bytearray(pad_value, 'utf-8')
        f.write(pad_value)
    # f.seek(0x13B2B)
    # # f.write(binascii.hexlify(b'hello world'))
    # f.write(b'RANDO HYPE') # Be careful of the number of characters we use... 
    # f.seek(0x13B3C)
    # # f.write(binascii.hexlify(b'Line 2'))
    # f.write(b'LINE 2 Plus more info')
    # f.seek(0x143B9)
    # # f.write(binascii.hexlify(b'seed info'))
    # f.write(b'SEED INFO567890')

print(output_rom_location)