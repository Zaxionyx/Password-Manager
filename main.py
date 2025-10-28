#import numpy as np
import random as ran
#import secrets as sec
from urllib import request
# def website():
#     website = input("Enter website name: ") 
#     url = f"{website}.com"
    

def password_generator():
    
    #choice = input("Would you like to generate a random password? ")
    #if choice == "yes":
        
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000" # A word site from the internet 
        response = request.urlopen(word_site) # The reponse requests the url to open from word site
        txt = response.read() # downloads the webpage data in bytes from the URL
        words = txt.decode().splitlines() #converts the bytes into readable texts then splits into one word
        random_word = ran.choice(words)
        random

    
        

       
        
       
    # elif choice == "no":
    #     return False
    
        


"""""
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
"""""




#strength_password()
password_generator()


















# def store():
#     txt_data = add_password()
#     file_path = "pwd0.txt"

#     with open(file_path, "r") as file: 
#         pass 

    




        
        
        
        
        

      

      
        

          
    