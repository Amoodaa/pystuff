single_uppercase_letter = input('Enter a single uppercase letter: ')

if (len(single_uppercase_letter) > 1) | (single_uppercase_letter.upper() != single_uppercase_letter):
    print("You did not comply with the request.")
else:
    print("Valid input")


# PS D:\code\pystuff\assignment> python .\118-35-input-validation.py
# Enter a single uppercase letter: A
# Valid input

# PS D:\code\pystuff\assignment> python .\118-35-input-validation.py
# Enter a single uppercase letter: sfa
# You did not comply with the request.

# PS D:\code\pystuff\assignment> python .\118-35-input-validation.py
# Enter a single uppercase letter: s
# You did not comply with the request.
