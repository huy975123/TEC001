def cabin_details():
    code = input("Enter the cabin class (LUX, A, B, C): ")
    
    if code == "LUX":
        print("upper-deck cabin with a balcony.")
    elif code == "A":
        print("above the car deck, equipped with a window.")
    elif code == "B":
        print("windowless cabin above the car deck.")
    elif code == "C":
        print("windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")

cabin_details()