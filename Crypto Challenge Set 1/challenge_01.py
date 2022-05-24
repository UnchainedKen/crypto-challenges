from base64 import b64encode
from binascii import unhexlify

def hex_to_base64(hexString: bytes) -> bytes:
    """Converts hex to base64"""
    return b64encode(unhexlify(hexString))


if __name__ == "__main__":
    output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    hexBytes = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    out = hex_to_base64(hexBytes)
    assert output == out
    print(out)

