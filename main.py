#import numpy as np
import random as ran
#import secrets as sec
import string
 
# def website():
#     website = input("Enter website name: ") 
#     url = f"{website}.com"

def password_generator():
    
    random_string = ""
    while True:
        choice = input("Do you want to generate a password? ")
        if choice == "yes":
            string_length = int(input("Random String Length: "))
            if string_length >= 5:
                possible_characters = input("Possible Characters: ")
                random_string += ran.choice(possible_characters)
                print(f"Generated password: {string_length, possible_characters}")
                break
        elif choice == "no":
         return password_generator()             
                   
def strength_password():
    generator_choice = password_generator()
    
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

























    




        
        
        
        
        

      

      
        

          
    