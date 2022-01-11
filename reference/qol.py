
# Enables instant text in most cases.
TEXT_SCROLL = [
    {
        'address': 0x02796C,
        'note': 'General text speed set at game start. Covers 90 percent of text boxes.',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x025F0F,
        'note': 'Dr Leo before he explodes Slow text start.',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x025F19,
        'note': 'Dr Leo after explode text speed restore',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x026004,
        'note': 'Dr Leo before death slow text',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x02600E,
        'note': 'Dr Leo post death text speed restore',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x02796C,
        'note': 'General text speed. Covers 90 percent of text boxes.',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x00'
        },
        'credit': 'Tranqulite'
    },
    {
        'address': 0x01BA48,
        'note': 'In Green Wood. "You" are on the menu',
        'speed': {
            'normal': b'\x03',
            'fast': b'\x02',
            'faster': b'\x01',
            'instant': b'\x01' # Can't be speed 0, so "instant" turns into faster.
        },
        'credit': 'Tranqulite'
    }
]

# For now, not making any changes to the credits text speed. 
# These addresses will allow us to alter the speed up to "faster"
# Must not be Speed 0
# 0053AF Post deathtoll defeat. Begin Epilogue autotext.
# 01B356 Post Credits Text Speed change. For speech given by Master.
# 01B38F Post Credits Text Speed change. Lisa talks with Turbo the Goat
# 01B3FD Post Credits Text Speed change. Lisa sees MC.
# 01B407 Post Credits Text Speed change. Restore Text Speed right after.
# 01B45C Post Credits Text Speed change. Turbo the Goat goes Bleeeet.
# 01B466 Post Credits Text Speed change. Restore Text Speed right after.
