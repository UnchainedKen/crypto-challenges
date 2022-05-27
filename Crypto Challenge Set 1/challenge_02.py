from binascii import hexlify, unhexlify

def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    """Function takes two equal-length buffer and produces their XOR combination"""
    
    # Checks string has same length
    assert(len(buffer1) == len(buffer2)), "Length of buffer does not equal"

    xored: str = ""
    for each in range(0, len(buffer1), 2):
        xored += chr(ord(unhexlify(buffer1[each:each+2])) ^ ord(unhexlify(buffer2[each:each+2])))

    try:
        xored = bytes(xored.encode("ascii"))
    except UnicodeEncodeError:
        xored = bytes(xored.encode("utf8"))
    return xored
    

if __name__ == "__main__":
    buff1 = b"1c0111001f010100061a024b53535009181c"
    buff2 = b"686974207468652062756c6c277320657965"
    output2 = b"746865206b696420646f6e277420706c6179"
    out = fixed_xor(buff1, buff2)
    assert output2 == hexlify(out)
    print(hexlify(out))

