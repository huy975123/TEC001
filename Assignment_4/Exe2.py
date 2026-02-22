number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    check = True
    for i in range(2, number):
        if number % i == 0:
            check = False
            break
    
    if check:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")