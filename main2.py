def caesar_cipher(text, key1, key2, mode):
    if not (1 <= key1 <= 25):
        print("Key 1 must be between 1 and 25.")
        return ""

    if not (key2.isalpha() and len(key2) >= 7 and key2.islower()):
        print("Key 2 must consist of at least 7 lowercase alphabetic characters.")
        return ""

    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    result = ""
    key2_index = 0

    for char in text:
        if 'A' <= char <= 'Z':
            if mode == 1:  # Encryption
                shift1 = key1
                shift2 = ord(key2[key2_index]) - ord('a') + 1
                encrypted_char = chr(((ord(char) - ord('A') + shift1 + shift2) % 26) + ord('A'))
                result += encrypted_char
                key2_index = (key2_index + 1) % len(key2)
            elif mode == 2:  # Decryption
                shift1 = key1
                shift2 = ord(key2[key2_index]) - ord('a') + 1
                decrypted_char = chr(((ord(char) - ord('A') - shift1 - shift2) % 26) + ord('A'))
                result += decrypted_char
                key2_index = (key2_index + 1) % len(key2)
        else:
            print(f"The character '{char}' is not valid and will be ignored.")

    return result

def main():
    mode = int(input("Enter the mode (1 for encryption, 2 for decryption): "))
    if mode not in [1, 2]:
        print("The mode entered is not valid. Please enter 1 for encryption or 2 for decryption.")
        return

    key1 = int(input("Enter key 1 (1-25): "))
    key2 = input("Enter key 2 (minimum 7 lowercase alphabetic characters): ")
    text = input("Enter the text: ")

    if mode == 1:
        encrypted_text = caesar_cipher(text, key1, key2, 1)
        print(f"Encrypted text: {encrypted_text}")
    elif mode == 2:
        decrypted_text = caesar_cipher(text, key1, key2, 2)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
