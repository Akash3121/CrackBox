def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            # Determine the shift based on the corresponding letter in the key
            shift = ord(key[i % key_length].upper()) - ord('A')
            
            # Encrypt the letter using the Caesar cipher mechanism
            if char.isupper():
                cipher_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                cipher_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # Preserve non-alphabetic characters
            cipher_text += char
    
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            # Determine the shift based on the corresponding letter in the key
            shift = ord(key[i % key_length].upper()) - ord('A')
            
            # Decrypt the letter using the Caesar cipher mechanism
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # Preserve non-alphabetic characters
            decrypted_text += char
    
    return decrypted_text

# Example usage:
plaintext = "Bloody Hell!" # Enter the text you want to encrypt here
keyword = "kaboom" # Enter the key here
encrypted_text = vigenere_encrypt(plaintext, keyword)
print("Encrypted Text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Decrypted Text:", decrypted_text)
