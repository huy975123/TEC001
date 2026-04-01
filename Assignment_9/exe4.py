def caesar_cipher(filename, n, direction):
    try:
        f = open(filename, 'r', encoding='utf-8')
        content = f.read() 
        f.close()
        
        result = ""
        for char in content:
            if char.isalpha():
                x = ord(char)
                if direction == "right":
                    if char.isupper():
                        y = (x + n - 65) % 26 + 65
                    else:
                        y = (x + n - 97) % 26 + 97
                elif direction == "left":
                    if char.isupper():
                        y = (x - n - 65) % 26 + 65
                    else:
                        y = (x - n - 97) % 26 + 97
                
                result += chr(y)
            elif char.isdigit():
                result += char 
            else:
                result += char
                
        out_filename = "cipher_" + filename
        out_file = open(out_filename, 'w', encoding='utf-8')
        out_file.write(result)
        out_file.close()
        
        return "Encryption successful, save in file: " + out_filename
    except FileNotFoundError:
        return "FileNotFoundError"