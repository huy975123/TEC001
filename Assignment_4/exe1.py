numbers = []

while True:
    user_input = input("Enter a number (empty string to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("The five greatest numbers are:", numbers[:5])