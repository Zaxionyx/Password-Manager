#import numpy as np
import random as ran
#import secrets as sec
import string
 
# def website():
#     website = input("Enter website name: ") 
#     url = f"{website}.com"

def password_generator():
    
    random_string = ""
    
    string_length = int(input("Random String Length: "))
    if string_length >= 5:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
        random_string = ''.join(ran.choice(characters) for i in range(string_length))
        print(f"Generated Password String for the length of {string_length}: {random_string}")
     
def strength_password():
    user = input("Enter username: ")
    special_chars = '!@#$%^&*()-+_=,'

    
    while True:
        password = input("Enter password: ")
        if len(password) < 5:
            print("The length of password is less than 5 characters.")
            continue
        elif not any(char.isupper() for char in password):
            print("Password does not include any uppercase letters")
            continue
        elif not any(char.islower() for char in password):
            print("Password does not include any lowercase letters")
            continue
        elif  not any(char in special_chars for char in password):
            print("Password does not include speical characters")
            continue
        elif not any(char.isdigit() for char in password):
            print("Password does not include any number")
        else:
            print("Password is strong enough")
        break
    print(f" Username: {user} \n Password: {password}")


choice = input(("Welcome to password manager! \n This is where you can generate a strong password, Check your password strength, and many more to come! \n Input 1: Generate Password \n Input 2: Check Password Strength \n "))
if choice == "1":
     password_generator()
elif choice == "2":
     strength_password()