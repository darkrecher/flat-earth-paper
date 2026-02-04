
XOR_KEY = b"obfuscation de la choucrouterie ultime !! 834513259765410 TONNERRE DE CHABRAQUE!!"

def decode(filename):
    encoded_data = open(filename, "r").read()
    bin_values = [
        int(a + b, 16) for a, b in zip(encoded_data[::2], encoded_data[1::2])
    ]
    bin_data = bytes(bin_values)
    mul_key = len(bin_data) // len(XOR_KEY) + 1
    xored_ints = [
        a ^ b for a, b in zip(bin_data, XOR_KEY * mul_key)
    ]
    str_clear = bytes(xored_ints).decode("utf-8")
    return str_clear

python_code_graphql_server = decode("graphql_server_enc.txt")
exec(python_code_graphql_server)

