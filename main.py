def caesar_cipher(text, key, mode):
    if not 1 <= key <= 25:
        print("The key must be between 1 and 25.")
        return ""

    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            if mode == 1:  # Encryption
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
                result += encrypted_char
            elif mode == 2:  # Decryption
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
                result += decrypted_char
        else:
            print(f"The character '{char}' is not valid and will be ignored.")

    return result

def main():
    mode = int(input("Enter the mode (1 for encryption, 2 for decryption): "))
    if mode not in [1, 2]:
        print("The mode entered is not valid. Please enter 1 for encryption or 2 for decryption.")
        return

    key = int(input("Enter the key (1-25): "))
    text = input("Enter the text: ")

    if mode == 1:
        encrypted_text = caesar_cipher(text, key, 1)
        print(f"Encrypted text: {encrypted_text}")
    elif mode == 2:
        decrypted_text = caesar_cipher(text, key, 2)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
