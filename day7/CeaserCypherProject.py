class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt_char(self, char):
        if char.isupper():
            return chr((ord(char) - 65 + self.shift) % 26 + 65)
        elif char.islower():
            return chr((ord(char) - 97 + self.shift) % 26 + 97)
        else:
            return char

    def decrypt_char(self, char):
        if char.isupper():
            return chr((ord(char) - 65 - self.shift) % 26 + 65)
        elif char.islower():
            return chr((ord(char) - 97 - self.shift) % 26 + 97)
        else:
            return char

    def encrypt(self, text):
        return "".join(self.encrypt_char(c) for c in text)

    def decrypt(self, text):
        return "".join(self.decrypt_char(c) for c in text)

    @staticmethod
    def brute_force(text):
        print("\n--- Brute Force Results ---")
        for shift in range(1, 26):
            cipher = CaesarCipher(shift)
            print(f"Shift {shift}: {cipher.decrypt(text)}")


def encrypt_file(filename, shift):
    try:
        with open(filename, "r") as file:
            data = file.read()

        cipher = CaesarCipher(shift)
        encrypted_data = cipher.encrypt(data)

        with open("encrypted_" + filename, "w") as file:
            file.write(encrypted_data)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found!")


def main():
    print("\n===== ADVANCED CAESAR CIPHER =====")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Brute Force Decryption")
    print("4. Encrypt File")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter choice: "))

            if choice == 1:
                text = input("Enter message: ")
                shift = int(input("Enter shift key: "))
                cipher = CaesarCipher(shift)
                print("Encrypted:", cipher.encrypt(text))

            elif choice == 2:
                text = input("Enter message: ")
                shift = int(input("Enter shift key: "))
                cipher = CaesarCipher(shift)
                print("Decrypted:", cipher.decrypt(text))

            elif choice == 3:
                text = input("Enter encrypted message: ")
                CaesarCipher.brute_force(text)

            elif choice == 4:
                filename = input("Enter filename: ")
                shift = int(input("Enter shift key: "))
                encrypt_file(filename, shift)

            elif choice == 5:
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter valid input!")


if __name__ == "__main__":
    main()
