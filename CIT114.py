class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, plaintext: str) -> str:
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - start + self.shift) % 26 + start)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext: str) -> str:
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - start - self.shift) % 26 + start)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text


# Example Usage
if __name__ == "__main__":
    shift_value = 3  # You can adjust the shift value
    cipher = CaesarCipher(shift_value)

    # Encrypting
    plaintext = "Hello, World!"
    encrypted_text = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted_text}")

    # Decrypting
    decrypted_text = cipher.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")
