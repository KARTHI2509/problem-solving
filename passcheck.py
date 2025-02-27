def check_password_validity(password):
    errors = []  
    if len(password) < 6 or len(password) > 12:
        errors.append("Password length must be between 6 and 12 characters.")
    
    lower = False
    upper = False
    digit = False
    special = False
    
    for char in password:
        if 'a' <= char <= 'z':
            lower = True
        elif 'A' <= char <= 'Z':
            upper = True
        elif '0' <= char <= '9':
            digit = True
        elif char in "$#@":
            special = True

    if not lower:
        errors.append("Your password doesn't have lowercase characters.")
    if not upper:
        errors.append("Your password doesn't have uppercase characters.")
    if not digit:
        errors.append("Your password doesn't have digits.")
    if not special:
        errors.append("Your password doesn't have special characters ($, #, @).")
    
    
    if errors:
        for error in errors:
            print(error)
        return False
    
    return True  

def validate_passwords(passwords):
    password_list = [password.strip() for password in passwords.split(',')]  # Split and trim spaces
    valid_passwords = [password for password in password_list if check_password_validity(password)]
    
    if valid_passwords:
        return ",".join(valid_passwords) 
    else:
        return None 


input_passwords = input("Enter passwords (comma separated): ")
output = validate_passwords(input_passwords)


if output:
    print("Valid passwords:", output)
else:
    print("Check your passwords, none are valid.")
