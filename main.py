from string import punctuation

def add_password(web, user, password):
    website = input("Enter website name: ")
    url = f"{website}.com"
    user = input("Enter username: ")
    special_chars = '!@#$%^&*()-+_=,'
    password = input("Enter password: ")
    while True:
        if len(password) < 5:
            print("The length of password is less than 5 characters.")
        
        elif  any(char not in special_chars for char in password):
            print("Password does not include speical characters")

        

          
    