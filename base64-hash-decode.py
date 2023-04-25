import base64

# Base64 encoded string
encoded_string = "aGFja2VydmVnYXMwMDEK"

# Decode the string
decoded_string = base64.b64decode(encoded_string)

# Convert bytes to string
decoded_string = decoded_string.decode('utf-8')

# Print the decoded string
print(decoded_string)
