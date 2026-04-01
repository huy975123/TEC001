def count_lines(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        count = 0
        for line in f:
            if len(line.strip()) > 0:
                count += 1
        f.close()
        return count
    except FileNotFoundError:
        return "FileNotFoundError"