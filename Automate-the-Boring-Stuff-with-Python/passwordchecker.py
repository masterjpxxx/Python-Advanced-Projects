import re


def passwordchecker(password):
    passwordregex = re.compile(r'''(
        ^(?=.*[A-Za-z])         # Checking for atleast one letter
        (?=.*\d)                # Checking for atleast one digit
        (?=.*[@$!%*#?&])        # Checking for one special character
        [A-Za-z\d@$!%*#?&]{8,}$ # Checking for combination of letters, digits and special characters annd 8 characters
        )''', re.VERBOSE)
    match = re.match(passwordregex, password)
    if match:
        print("Strong Password Detected!")
    else:
        print("Password strength is too low. Please revise your password")
        

while(True):
    password = input('Please input a password: ')
    passwordchecker(password)