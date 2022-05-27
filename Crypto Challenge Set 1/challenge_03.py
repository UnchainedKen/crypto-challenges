from binascii import hexlify, unhexlify
from typing import Tuple, List, Optional
from dataclasses import dataclass, astuple

from challenge_02 import fixed_xor


freq = {
    "a": 0.07720023509302927,
    "b": 0.014003367395322557,
    "c": 0.02674325172273787,
    "d": 0.0489691965667332,
    "e": 0.13423868756761054,
    "f": 0.025198679163318673,
    "g": 0.017137941118849746,
    "h": 0.057234363332301724,
    "i": 0.063157117668604,
    "j": 0.0012464473411489463,
    "k": 0.005073807286180334,
    "l": 0.03701295567019969,
    "m": 0.030266807873912907,
    "n": 0.07136549867831153,
    "o": 0.07417071501784492,
    "p": 0.017453102063878297,
    "q": 0.0009426435472925972,
    "r": 0.060848776692854364,
    "s": 0.061408116388085215,
    "t": 0.08756363553766174,
    "u": 0.030471236595012507,
    "v": 0.011152722451100366,
    "w": 0.021734748055797684,
    "x": 0.001984662167341944,
    "y": 0.02282787385612193,
    "z": 0.0005934111487474482
}

@dataclass(order=True)
class BestGuess:
    score: float = float("inf")
    key: Optional[int] = None
    ciphertext: Optional[bytes] = None
    plaintext: Optional[bytes] = None

    @classmethod
    def from_key(cls, cipher, key_val):
        full_key = bytes([key_val]*(len(cipher)//2))
        plain = fixed_xor(hexlify(full_key), cipher)
        score = score_text(plain)
        return cls(score, key_val, cipher, plain)

def score_text(text: bytes) -> float:
    score = 0.0
    l = len(text)

    for letter, freq_expected in freq.items():
        freq_actual = text.count(ord(letter)) / l
        err = abs(freq_expected - freq_actual)
        score += err
    return score

def single_byte_xor_cipher_simple(ciphertext: bytes) -> BestGuess:
    """The hex encoded cipher string: has been XOR'd against a single character. 
    Find the key, decrypt the message. 
    """
    best_guess = BestGuess()

    for candidate_key in range(256):
        guess = BestGuess.from_key(ciphertext, candidate_key)
        best_guess = min(best_guess, guess)
    return best_guess

def xor_cipher_crack_complex(cipher: bytes)-> BestGuess:
    best_guess = BestGuess()

    cipher_len = len(cipher)
    cipher_freq = {byte: unhexlify(cipher).count(byte)/cipher_len for byte in range(256)}
    
    for candidate_key in range(256):
        score = 0
        for letter, freq_expected in freq.items():
            score += abs(freq_expected - cipher_freq[ord(letter) ^ candidate_key])
        guess = BestGuess(score, candidate_key)
        best_guess = min(best_guess, guess)

    best_guess.ciphertext = cipher
    best_guess.plaintext = fixed_xor(hexlify(bytes([best_guess.key]*(cipher_len//2))), cipher )
    return best_guess

if __name__ == "__main__":
    cipher = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    #? Using Simple crack
    best = single_byte_xor_cipher_simple(cipher)
    score, key,  ciphertext, plaintext = astuple(best)
    print(f"{key = }")
    print(f"{plaintext = }")

    #? Complex
    best2 = xor_cipher_crack_complex(cipher)
    print(f"{best2.key = }")
    print(f"{best2.plaintext = }")
