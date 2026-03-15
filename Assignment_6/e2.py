seasons = ("spring", "summer", "autumn", "winter")
month = int(input("Enter a month (1-12): "))

if month == 3 or month == 4 or month == 5:
    season = seasons[0]
elif month == 6 or month == 7 or month == 8:
    season = seasons[1]
elif month == 9 or month == 10 or month == 11:
    season = seasons[2]
elif month == 12 or month == 1 or month == 2:
    season = seasons[3]
else:
    season = "Invalid"

if season != "Invalid":
    print("The season is:", season)
  
