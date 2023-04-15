import generate_password 
length_password=int(input("minimum entry 10 characters: "))
if length_password < 10:
    print("password not accepted")
else:
    password=generate_password.generate_password(length_password)
    print(password)

