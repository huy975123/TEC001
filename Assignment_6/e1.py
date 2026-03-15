numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    numbers.append(int(user_input))

numbers.sort(reverse=True)
print("Top 5 greatest numbers:", numbers[:5])

