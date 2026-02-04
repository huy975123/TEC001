def get_acronym(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result = result + word[0]
    return result.upper()

user_input = input("Enter a phrase: ")
print(get_acronym(user_input))
