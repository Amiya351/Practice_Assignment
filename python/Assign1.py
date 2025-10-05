import re

def check_password_strength(password):
    #Check minimum length(at least 8 characters)
    if len(password)< 8:
        return False
    
    #Check for at leeast one uppercase letter
    if not re.search(r'[A-Z]',password):
        return False
    
    #Check for at least one lowercase letter
    if not re.search(r'[a-z]',password):
        return False
    
    #Check for at least one digit
    if not re.search(r'\d',password):
        return False
    
    #Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]',password):
        return False
    return True

def get_password_feedback(password):
    issues = []

    #Check each criterion and collect issues
    if len(password)< 8:
        issues.append("❌ Password must be at least 8 characters long")
    else:
        issues.append("Length requirement met")
    if not re.search(r'[A-Z]', password):
        issues.append("❌ Password must contain at least one uppercase letter")
    else:
        issues.append("Contains uppercase letter")
    if not re.search(r'[a-z]',password):
        issues.append("❌ Password must contain at least one lowercase letter")
    else:
        issues.append("Contains lowercase letter")
    if not re.search(r'\d', password):
        issues.append("❌ Password must contain at least one digit (0-9)")
    else:
        issues.append("Contains digit")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        issues.append("❌ Password must contain at least one special character (!@#$%...)")
    else:
        issues.append("Contains special character")
    
    is_strong = check_password_strength(password)
    return is_strong, issues

def main():
    """Main function to run the password strength checker."""
    print("=" * 50)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print("\nPassword Requirements:")
    print("  • Minimum 8 characters")
    print("  • At least one uppercase letter (A-Z)")
    print("  • At least one lowercase letter (a-z)")
    print("  • At least one digit (0-9)")
    print("  • At least one special character (!@#$%...)")
    print("=" * 50)
    
    while True:
        # Get password input from user
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker!")
            break
        
        if not password:
            print("\n Password cannot be empty. Please try again.")
            continue
        
        # Check password strength and get feedback
        is_strong, feedback = get_password_feedback(password)
        
        print("\n" + "-" * 50)
        print("Password Strength Analysis:")
        print("-" * 50)
        
        for item in feedback:
            print(f"  {item}")
        
        print("-" * 50)
        
        if is_strong:
            print("\n SUCCESS! Your password is strong!")
        else:
            print("\n WARNING! Your password is weak.")
            print("Please address the issues marked with ❌")
        
        print()

if __name__ == "__main__":
    main()