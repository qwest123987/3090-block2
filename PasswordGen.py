import random
import string

def generate_password(length):
    valid_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(valid_chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
