# UTF-8 and UTF-16 decoding script in Python

# Define the encoded string
encoded_string = b'\xc3\xa9\xc3\xa0' # UTF-8 encoded string

# Decode the UTF-8 string
decoded_string = encoded_string.decode('utf-8')
print(decoded_string)

# Define the encoded string
encoded_string = b'\xff\xfe\xe9\x00\xe0\x00' # UTF-16 encoded string

# Decode the UTF-16 string
decoded_string = encoded_string.decode('utf-16')
print(decoded_string)
