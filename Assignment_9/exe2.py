def find_keyword(filename, keyword):
    try:
        f = open(filename, 'r', encoding='utf-8')
        line_numbers = []
        line_idx = 1
        
        for line in f:
            if keyword in line:
                line_numbers.append(line_idx)
            line_idx += 1
            
        f.close()
        return line_numbers
    except FileNotFoundError:
        return "FileNotFoundError"