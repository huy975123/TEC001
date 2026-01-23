def check_zander():
    length = float(input("Enter the length of the zander (cm): "))
    
    limit = 42
    
    if length >= limit:
        print("The zander meets the size limit.")
    else:
        diff = limit - length
        print("Release the fish back into the lake.")
        print(f"The fish was {diff} cm below the size limit.")

check_zander()