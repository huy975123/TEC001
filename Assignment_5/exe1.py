import re

def check_course_code(code):
    if re.search("^[A-Z]{2,3}[0-9]{3}$", code):
        return True
    else:
        return False
    
