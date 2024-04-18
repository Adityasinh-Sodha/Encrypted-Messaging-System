def encode_text(text, mapping):
    encoded_text = ""
    for char in text:
        if char in mapping:
            encoded_text += mapping[char]  # Append the mapped value to encoded_text
        else:
            encoded_text += char  # Keep the character unchanged if not in mapping
    return encoded_text

def decode_text(encoded_text, mapping):
    reverse_mapping = {value: key for key, value in mapping.items()}
    decoded_text = ""
    encoded_sequence = ""
    
    for char in encoded_text:
        encoded_sequence += char  # Build up the sequence of encoded characters
        if encoded_sequence in reverse_mapping:
            decoded_text += reverse_mapping[encoded_sequence]  # Append decoded character
            encoded_sequence = ""  # Reset for the next sequence
    
    return decoded_text

# Custom mapping You can write Your own mapping Here!
custom_mapping = {
    'A': '468027',
    'B': '910364',
    'C': '580031',
    'D': '270456',
    'E': '392070',
    'F': '800519',
    'G': '720531',
    'H': '140690',
    'I': '630724',
    'J': '950012',
    'K': '308176',
    'L': '570382',
    'M': '810947',
    'N': '200538',
    'O': '701625',
    'P': '390470',
    'Q': '850061',
    'R': '160259',
    'S': '309562',
    'T': '470836',
    'U': '936001',
    'V': '700235',
    'W': '410578',
    'X': '608025',
    'Y': '283105',
    'Z': '750960',
    ' ': '540263',
    'a': '204896',
    'b': '610452',
    'c': '935201',
    'd': '407613',
    'e': '915024',
    'f': '203786',
    'g': '598061',
    'h': '170349',
    'i': '685019',
    'j': '402357',
    'k': '790510',
    'l': '310204',
    'm': '590081',
    'n': '200638',
    'o': '710492',
    'p': '306857',
    'q': '980015',
    'r': '640125',
    's': '530098',
    't': '780503',
    'u': '610092',
    'v': '408513',
    'w': '279061',
    'x': '508309',
    'y': '304612',
    'z': '802745',
    '1': '638091',
    '2': '591047',
    '3': '820400',
    '4': '357902',
    '5': '194607',
    '6': '750031',
    '7': '500382',
    '8': '810625',
    '9': '239084',
    '0': '570136',
    '!': '920704',
    '@': '462501',
    '#': '715390',
    '$': '846302',
    '%': '359024',
    '^': '180236',
    '&': '500128',
    '*': '793015',
    '(': '628705',
    ')': '437190',
    '_': '362040',
    '': '581260',
    '-': '204639',
    '=': '910583',
    '~': '783015',
    '`': '502801',
    '{': '619350',
    '}': '470826',
    '|': '370198',
    '[': '250963',
    ']': '860315',
    '\\': '510028',
    ':': '690248',
    '"': '305187',
    ';': '106294',
    "'": '970035',
    '>': '541082',
    '?': '302857',
    '<': '475903',
    ',': '603921',
    '.': '518307',
    '/': '206479',
    '*': '895702',
    '|': '507391',
    '\\': '037641',
    '"': '928603',
    '\\': '157309',
}

# Text to encode Write Your Message Here!
text_to_encode = "Hello World!"

encoded_text = encode_text(text_to_encode, custom_mapping)
print("Encoded Text:", encoded_text)

# Encoded text to decode; Decode The Encoded Text Here!
encoded_text_to_decode = "140690915024310204310204710492540263410578710492640125310204407613920704"
decoded_text = decode_text(encoded_text_to_decode, custom_mapping)
print("Decoded Text:", decoded_text)

#Thank you for using my code. If you found it helpful, please consider starring this repository. Your support is greatly appreciated!
