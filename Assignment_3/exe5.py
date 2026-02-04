attempts = 0
correct_user = "python"
correct_pass = "rules"

while attempts < 5:
    user = input("Username: ")
    password = input("Password: ")
    
    if user == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        attempts = attempts + 1
        if attempts == 5:
            print("Access denied")
            