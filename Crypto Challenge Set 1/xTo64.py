import base64 

HEX_TO_INT = int

def hex_to_base64(hexString: str) -> bytes:
    """Comverts hex to base64"""

    #  Converted hex ascii string and empty string for converted hex
    ascii_string: str = ""

    # Start Conversion loop
    for each in range(0, len(hexString), 2):
        ascii_string += chr(HEX_TO_INT(f"0x{hexString[each:each+2]}", 16))
    return base64.b64encode(ascii_string.encode("ascii"))

def fixed_xor(buffer1: str, buffer2: str) -> str:
    """Function takes two equal-length buffer and produces their XOR combination"""

    # Checks string has same length
    assert(len(buffer1) == len(buffer2))
    
    result: str = ""
    for each in range(0, len(buffer1), 2):
        result += hex(HEX_TO_INT(f"0x{buffer1[each:each+2]}",16) ^ HEX_TO_INT(f"0x{buffer2[each:each+2]}",16)).lstrip("0x")
    return result

def main():
    #? Test hex_to_base64 function
    output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert(output == hex_to_base64(hexString))

    #? Test fixed_xor function
    buff1 = "1c0111001f010100061a024b53535009181c"
    buff2 = "686974207468652062756c6c277320657965"
    output2 = "746865206b696420646f6e277420706c6179"
    assert(output2 == fixed_xor(buff1, buff2))

if __name__ == "__main__":
    main()
