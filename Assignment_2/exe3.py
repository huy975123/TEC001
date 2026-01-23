def check_hemoglobin():
    gender = input("Enter your biological sex (female/male): ")
    hg_value = int(input("Enter hemoglobin value (g/l): "))
    
    if gender == "female":
        if hg_value < 117:
            print("Hemoglobin value is low.")
        elif hg_value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
            
    elif gender == "male":
        if hg_value < 134:
            print("Hemoglobin value is low.")
        elif hg_value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid gender input.")


check_hemoglobin()