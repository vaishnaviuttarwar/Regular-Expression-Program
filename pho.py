import re

phone_regex='^(\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
phone_number=input("Enter the number")
match=re.search(phone_regex, phone_number)

if(match==None):
    print("Invalid Number")
else:
    print("Valid Number")