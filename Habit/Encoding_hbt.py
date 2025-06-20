custom_encoding = {
    'a': b'\x02',
    'b': b'\x01',
    'c': b'\x06',
    'd': b'\x1D',
    'e': b'\x1C',
    'f': b'\x03',
    'g': b'\x08',
    'h': b'\x07',
    'i': b'\x1A',
    'j': b'\x0A',
    'k': b'\x0B',
    'l': b'\x0C',
    'm': b'\x0D',
    'n': b'\x0E',
    'o': b'\x0F',
    'p': b'\x10',
    'q': b'\x11',
    'r': b'\x12',
    's': b'\x13',
    't': b'\x14',
    'u': b'\x15',
    'v': b'\x16',
    'w': b'\x17',
    'x': b'\x18',
    'y': b'\x19',
    'z': b'\x21',
    ':': b'\x22',
    ' ': b'\x20',
    '-' : b'\x31',
    '1' : b'\x32',
    '2' : b'\x33',
    '3' : b'\x34',
    '4' : b'\x35',
    '5' : b'\x36',
    '6' : b'\x37',
    '7' : b'\x38',
    '8' : b'\x39',
    '9' : b'\x3A',
    '0' : b'\x3B',
    '\n' : b'\x7F',
}

# Reverse lookup for decoding
custom_decoding = {v: k for k, v in custom_encoding.items()}

def encode_custom(text):
    encoded = b''
    for char in text:
        if char in custom_encoding:
            encoded += custom_encoding[char]
        else:
            raise ValueError(f"Char {char!r} not supported")
    return encoded

def decode_custom(data):
    decoded = ''
    for byte in data:
        key = bytes([byte])
        if key in custom_decoding:
            decoded += custom_decoding[key]
        else:
            raise ValueError(f"Byte {byte:#x} not supported")
    return decoded