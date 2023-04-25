def decode_hex(hex_string):
    # Convert the hexadecimal string to a bytes object
    hex_bytes = bytes.fromhex(hex_string)

    # Convert the bytes object to an ASCII string
    ascii_string = hex_bytes.decode('ascii')

    return ascii_string

# Example usage
hex_string = '48656c6c6f20576f726c64'
ascii_string = decode_hex(hex_string)
print(ascii_string)
