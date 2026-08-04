import re
def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False

def validate_phone_number(phone_number):
    # Regular expression for validating a phone number
    regex = r'^\+?[0-9]{10,15}$'

    if re.match(regex, phone_number):
        return True
    else:
        return False