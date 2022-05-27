from typing import Optional, Tuple, Text

from challenge_03 import single_byte_xor_cipher_simple, xor_cipher_crack_complex


def detect_single_char_xor(file: Text) -> bytes:
    """One of the 60-characters string in 
    file has been encrypted by single-character XOR
    """
    best_score: Tuple[float, bytes] = (float("inf"), None)

    with open(file, "r") as text:
        for line in text.readlines():
            result = xor_cipher_crack_complex(line.rstrip("\n").strip())
            curr = (result.score, result.plaintext)
            best_score = min(best_score, curr)

    return best_score[1]
    
if __name__ == "__main__":
    ptTup = detect_single_char_xor("4.txt")
    print(ptTup)
