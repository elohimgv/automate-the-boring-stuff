#! python3
import re, pyperclip

def strongPasswordDetection(text):
    # At least eight characters long regex
    password_long = re.compile(r'.{8,}')
    # Numeric digit regex
    numeric_digit_character = re.compile(r'[0-9]')
    # Upper letter regex
    upper_letter_character = re.compile(r'[A-Z]')
    # Lower letter regex
    lower_letter_character = re.compile(r'[a-z]')

    # Test matching object
    if password_long.search(text) == None:
        return False
    elif numeric_digit_character.search(text) == None:
        return False
    elif upper_letter_character.search(text) == None:
        return False
    elif lower_letter_character.search(text) == None:
        return False
    else:
        return True
        
# Find matches in clipboard text
text = str(pyperclip.paste())
# Call function
if strongPasswordDetection(text) == True:
    print('Strong password!')
else:
    print('Weak password!')
