largest = None
smallest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    
    num = float(user_input)
    
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Smallest:", smallest)
print("Largest:", largest)
