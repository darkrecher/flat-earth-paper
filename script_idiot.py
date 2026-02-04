XOR_KEY = b"obfuscation de la choucrouterie ultime !! 834513259765410 TONNERRE DE CHABRAQUE!!"

def main():
    bin_data = open("graphql_server.py", "rb").read()
    mul_key = len(bin_data) // len(XOR_KEY) + 1
    xored_ints = [
        f"{a^b:02x}" for a, b in zip(bin_data, XOR_KEY * mul_key)
    ]
    file_out = open("graphql_server_enc.txt", "w")
    file_out.write("".join(xored_ints))
    file_out.close()


if __name__ == "__main__":
    main()
