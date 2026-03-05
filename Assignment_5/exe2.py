import re

def check_hex_color(color):
    if re.search("^#[0-9a-fA-F]{6}$", color):
        return True
    else:
        return False
    
    