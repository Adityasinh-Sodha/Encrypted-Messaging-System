from mapping import custom_mapping

def encode_text(text, mapping):
    encoded_chars = []
    for char in text:
        if char in mapping:
            encoded_chars.append(mapping[char])
        else:
            encoded_chars.append(char)  # Append the character unchanged
    return ''.join(encoded_chars)

def decode_text(encoded_text, mapping):
    reverse_mapping = {value: key for key, value in mapping.items()}
    decoded_text = []
    encoded_sequence = ""
    
    for char in encoded_text:
        encoded_sequence += char
        if encoded_sequence in reverse_mapping:
            decoded_text.append(reverse_mapping[encoded_sequence])
            encoded_sequence = ""
        # Add error handling for unmapped sequences if needed
    
    return ''.join(decoded_text)

# Prompt user for text to encode
text_to_encode = input("Enter text to encode: ")

# Encode the input text
encoded_text = encode_text(text_to_encode, custom_mapping)
print("Encoded Text:", encoded_text)

# Prompt user for encoded text to decode
encoded_text_to_decode = input("Enter encoded text to decode: ")

# Decode the input encoded text
decoded_text = decode_text(encoded_text_to_decode, custom_mapping)
print("Decoded Text:", decoded_text)
