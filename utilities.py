import json
import re
from datetime import datetime

def validate_email(email):
    email_regex = r'^\w+[\w\.]*@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    phone_regex = r'^(\+20|0020|0)1[0125][0-9]{8}$'
    return re.match(phone_regex, phone) is not None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
