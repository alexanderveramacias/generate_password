import string
import random

letters=string.ascii_letters
numbers=string.digits
characters=string.punctuation

def generate_password(length):
    all_characters=letters+numbers+characters
    password="".join(random.choice(all_characters) for index in range(length))
    return password