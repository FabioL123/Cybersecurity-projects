import re

def check_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error or digit_error or upper_error or lower_error or symbol_error:
        print("Password is weak. Suggestions:")
        if length_error: print("- Use at least 8 characters")
        if digit_error: print("- Add at least one digit")
        if upper_error: print("- Add at least one uppercase letter")
        if lower_error: print("- Add at least one lowercase letter")
        if symbol_error: print("- Add at least one special symbol")
    else:
        print("Password is strong!")

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    check_password(pwd)