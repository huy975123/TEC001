import re

def hide_phone_numbers(text):
    result = re.sub(r"\+84[0-9]+|[0-9]{10}", "[REDACTED]", text)
    return result


