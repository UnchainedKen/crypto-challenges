import base64 
import string

HEX_TO_INT = int

def hex_to_base64(hexString: str) -> bytes:
    """Converts hex to base64"""

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

def single_byte_xor_cipher(cipher: str) -> None:
    """The hex encoded cipher string: has been XOR'd against a single character. 
    Find the key, decrypt the message. 
    """
    plaintext: str = ""
    plaintext_list: list = []
    key: str = string.printable

    for k in range(len(key)):
        for char in range(0, len(cipher), 2):
            plaintext += chr(HEX_TO_INT(cipher[char:char+2], 16) ^ ord(key[k]))
        plaintext_list.append(f"{plaintext}: {key[k]}")
        print(plaintext_list[k])
        plaintext = ""

def ascii_to_hex(text: str) -> str:
    """Takes ascii/printable letters and return hex string"""
    hexString: str =""
    for char in range(len(text)):
        hexString += hex(ord(text[char])).lstrip("0x")
    return hexString

def main():
    #? Test hex_to_base64 function
    output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert(output == hex_to_base64(hexString).decode())

    #? Test fixed_xor function
    buff1 = "1c0111001f010100061a024b53535009181c"
    buff2 = "686974207468652062756c6c277320657965"
    output2 = "746865206b696420646f6e277420706c6179"
    assert(output2 == fixed_xor(buff1, buff2))

    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    # joke = ascii_to_hex("ETAOIN SHRDLU")
    single_byte_xor_cipher(cipher)

if __name__ == "__main__":
    main()
