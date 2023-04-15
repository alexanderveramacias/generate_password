import generate_password 
import colorama

print(colorama.Fore.LIGHTGREEN_EX+"welcome to password generator 😀 ")
length_password=int(input("minimum entry 10 characters: "))
if length_password < 10:
    print(colorama.Fore.RED+"password not accepted")
else:
    password=generate_password.generate_password(length_password)
    print(colorama.Fore.LIGHTCYAN_EX+password)
    print("this is the password that has been generated")


