def remove_odds(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def main():
    original_list = [10, 15, 22, 33, 40, 55, 60]
    cut_down_list = remove_odds(original_list)
    
    print("Original list:", original_list)
    print("Cut-down list:", cut_down_list)

main()

