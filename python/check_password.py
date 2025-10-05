import re

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%]', password):
        return False
    return True

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    if check_password_strength(pwd):
        print("Password is strong!")
    else:
        print("Password is weak. Make sure it is at least 8 characters long, contains uppercase and lowercase letters, at least one digit, and at least one special character (!, @, #, $, %).")