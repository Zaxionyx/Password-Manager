def website():
    website = input("Enter website name: ") 
    url = f"{website}.com"


    
def strength_password():
    website()
    
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





strength_password()

















# def store():
#     txt_data = add_password()
#     file_path = "pwd0.txt"

#     with open(file_path, "r") as file: 
#         pass 

    




        
        
        
        
        

      

      
        

          
    