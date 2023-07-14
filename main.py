def check_password(password):
    # Minimum length of the password
    if len(password) < 8:
        print("\U0001F612")
        return "Password is too short. It should be at least 8 characters long."

    # Check for uppercase letters
    if not any(c.isupper() for c in password):
        print("\U0001F641")
        return "Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(c.islower() for c in password):
        print("\U0001F641")
        return "Password should contain at least one lowercase letter."

    # Check for digits
    if not any(c.isdigit() for c in password):
        print("\U0001F641")
        return "Password should contain at least one digit."
        
    # Check for special characters
    special_chars = "!@#$%^&*()_-+={}[];:',.<>/?"
    if not any(c in special_chars for c in password):
        print("\U0001F641")
        return "Password should contain at least one special character."
        
    # Check for consecutive characters
    if any(substring in password.lower() for substring in ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']):
        print("\U0001F641")
        return "Password should not have consecutive characters."

    # If the password meets all criteria
    print("\U0001F60E")
    return "Password is strong."

# Running the code
password = input("Enter your password(A-Z,a-z,0-9,!@#$%^&*...):\n")

output = check_password(password)

print(output)
