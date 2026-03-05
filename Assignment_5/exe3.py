import re

def sum_of_numbers(paragraph):
    numbers = re.findall("[0-9]+", paragraph)
    total = 0
    for num in numbers:
        total = total + int(num)
    return total
