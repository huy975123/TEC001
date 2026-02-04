def get_middle(text):
    length = len(text)
    mid = length // 2
    
    if length % 2 == 0:
        return text[mid-1 : mid+1]
    else:
        return text[mid]

string_input = input("Enter a string: ")
result = get_middle(string_input)
print(result)
