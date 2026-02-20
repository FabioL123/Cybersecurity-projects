def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift number: "))
    print("Encrypted text:", caesar_encrypt(text, shift))