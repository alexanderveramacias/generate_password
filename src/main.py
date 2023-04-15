import string
import random
letters=string.ascii_letters
numbers=string.digits
characters=string.punctuation

def generate_password(length):
    all_characters=letters+numbers+characters
    print(all_characters)
generate_password(0)
