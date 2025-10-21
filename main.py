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
        
            print("Password is not strong enough, include a special character.")
        else:
            print("Password is strong enough.")
            break  