      characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
        random_string = ''.join(sec.choice(characters) for i in range(string_length))
        print(f"Generated Password String for the length of {string_length}: {random_string}")