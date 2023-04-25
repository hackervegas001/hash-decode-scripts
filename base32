import base64

def decode_base32(encoded_str):
    decoded_bytes = base64.b32decode(encoded_str)
    return decoded_bytes.decode('utf-8')

# Example usage
encoded_str = 'JBSWY3DPEBLW64TMMQQQ===='
decoded_str = decode_base32(encoded_str)
print(decoded_str)
