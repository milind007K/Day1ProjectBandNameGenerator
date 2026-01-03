import random
import string

# Character sets
letters = string.ascii_letters  # a-z + A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # !@#$%^&*()...

# Combine all characters
all_chars = letters + digits + symbols

# Ask user for desired length
length = int(input("Enter the password length: "))

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated Password:", password)
