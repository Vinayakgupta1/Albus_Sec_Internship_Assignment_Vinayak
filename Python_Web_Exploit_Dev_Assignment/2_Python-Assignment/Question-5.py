# Q.5 Write a Python script to generate strong passwords of a specified length, including a mix of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)

print("Generated password:", password)