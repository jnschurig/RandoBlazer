
# Enables instant text in most cases.
TEXT_SCROLL = [
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
    }
]
# Add these in later. This is all related to the text scroll speed.
# Courtesy of Tranquilite.
# Can be any speed
# 025F0F Dr Leo before he explodes Slow text start
# 025F19 Dr Leo after explode text speed restore
# 026004 Dr Leo before death slow text
# 02600E Dr Leo post death text speed restore
# 02796C Set at start of game. Text speed for most of game

# Must not be Speed 0
# 0053AF Post deathtoll defeat. Begin Epilogue autotext.
# 01B356 Post Credits Text Speed change. For speech given by Master.
# 01B38F Post Credits Text Speed change. Lisa talks with Turbo the Goat
# 01B3FD Post Credits Text Speed change. Lisa sees MC.
# 01B407 Post Credits Text Speed change. Restore Text Speed right after.
# 01B45C Post Credits Text Speed change. Turbo the Goat goes Bleeeet.
# 01B466 Post Credits Text Speed change. Restore Text Speed right after.
# 01BA48 In Green Wood. "You" are on the menu