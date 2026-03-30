import re

def check_length(password):
    return len(password) >= 8        

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))  

def check_digits(password):
    return bool(re.search(r'[0-9]', password))

def check_specialchar(password):
    return bool(re.search(r'[!@#$%^&*]', password))

def check_strength(password):
    print("\nAnalyzing your password...\n")

    criteria = {                                
        "Minimum 8 characters"   : check_length(password),
        "Uppercase letter (A-Z)" : check_uppercase(password),
        "Lowercase letter (a-z)" : check_lowercase(password),
        "Digits (0-9)"           : check_digits(password),
        "Special character (!@#)": check_specialchar(password),
    }

    passed = 0
    for rule, result in criteria.items():      
        status = "True" if result else "False"
        print(f"{status} {rule}")
        if result:
            passed += 1

    print("\n--- Result ---")                   
    if passed == 5:
        print("STRONG password! Great job.")
    elif passed >= 3:
        print("MEDIUM password. Try adding more variety.")
    else:
        print("WEAK password. Please make it stronger.")

    print(f"Score: {passed}/5\n")

# --- Run it ---
while True:
    password = input("Enter a password to check (or type 'quit' to exit): ")
    if password.lower() == 'quit':
        print("Goodbye!")
        break
    check_strength(password)
