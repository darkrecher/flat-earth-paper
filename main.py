XOR_KEY = b"obfuscation de la choucrouterie ultime !! 834513259765410 TONNERRE DE CHABRAQUE!!"

def encode_one_file(filename_in, filename_out):
    bin_data = open(filename_in, "rb").read()
    mul_key = len(bin_data) // len(XOR_KEY) + 1
    xored_ints = [
        f"{a^b:02x}" for a, b in zip(bin_data, XOR_KEY * mul_key)
    ]
    file_out = open(filename_out, "w")
    file_out.write("".join(xored_ints))
    file_out.close()


def main():
    encode_one_file("graphql_server.py", "graphql_server_enc.txt")
    encode_one_file("papers_fake_db.py", "papers_fake_db_enc.txt")


if __name__ == "__main__":
    main()

"""

curl -X POST https://flat-earth-paper.onrender.com/graphql -H "Content-Type: application/json"   -d '{"query": "{ article(articleId: \"paper_001\") { title issuerId keywords } }"}'

curl -X POST http://localhost:3000/graphql -H "Content-Type: application/json"   -d '{"query": "{ article(articleId: \"paper_001\") { title issuerId keywords } }"}'

"""
