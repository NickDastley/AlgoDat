

def decipher_string(ciphertext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = alphabet[11:] + alphabet[:11]
    shifted_word = ""

    for letter in ciphertext:
        if letter == " ":
            shifted_word += " "
            continue

        # find letter index in alphabet
        index = alphabet.index(letter)
        # append new letter to new word
        shifted_word += shifted_alphabet[index]

    return shifted_word

# Example usage:
ciphertext = "WTGPD NCJAEZRCLASJ DLGPD"
plaintext = decipher_string(ciphertext)
print("Deciphered string:", plaintext)