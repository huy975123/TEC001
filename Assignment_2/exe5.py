import math


def calculate_unit_price(diameter_cm, price_usd):
    radius_cm = diameter_cm / 2
    radius_m = radius_cm / 100  
    area = math.pi * (radius_m * radius_m)
    
    unit_price = price_usd / area
    return unit_price

def main_pizza():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))
    
    price_per_m2_1 = calculate_unit_price(d1, p1)
    price_per_m2_2 = calculate_unit_price(d2, p2)

    print(f"Pizza 1 unit price: {price_per_m2_1:.2f} USD/m2")
    print(f"Pizza 2 unit price: {price_per_m2_2:.2f} USD/m2")

    if price_per_m2_1 < price_per_m2_2:
        print("Pizza 1 provides better value for money.")
    elif price_per_m2_2 < price_per_m2_1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value.")

main_pizza()