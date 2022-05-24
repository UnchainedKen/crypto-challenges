from binascii import hexlify, unhexlify

def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    """Function takes two equal-length buffer and produces their XOR combination"""
    
    # Checks string has same length
    assert(len(buffer1) == len(buffer2)), "Length of buffer does not equal"
    # Decode data to work on raw buffers
    buffer1, buffer2 = buffer1.decode("ascii"), buffer2.decode("ascii")

    xored: str = ""
    for each in range(0, len(buffer1), 2):
        xored += chr(int(f"0x{buffer1[each:each+2]}",16) ^ int(f"0x{buffer2[each:each+2]}",16))
    return hexlify(xored.encode("ascii"))
    

if __name__ == "__main__":
    buff1 = b"1c0111001f010100061a024b53535009181c"
    buff2 = b"686974207468652062756c6c277320657965"
    output2 = b"746865206b696420646f6e277420706c6179"
    out = fixed_xor(buff1, buff2)
    assert(output2 == out)
    print(out)
