
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
        }
    }
]
