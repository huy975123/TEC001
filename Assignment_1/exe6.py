talents = float(input("Enter talents: \n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))

gram_from_talents = talents * 20 * 32 * 13.3
gram_from_pounds = pounds * 32 * 13.3
gram_from_lots = lots * 13.3

total_grams = gram_from_talents + gram_from_pounds + gram_from_lots

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")