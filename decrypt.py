def caesar_decrypt(text, shift):
    from encrypt import caesar_encrypt
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    text = input("Enter text to decrypt: ")
    shift = int(input("Enter shift number: "))
    print("Decrypted text:", caesar_decrypt(text, shift))