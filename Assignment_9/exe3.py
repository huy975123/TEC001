def calc_average(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        total_score = 0
        student_count = 0
        
        for line in f:
            line = line.strip()
            if len(line) > 0:
                parts = line.split(',')
                score = float(parts[1])
                total_score += score
                student_count += 1
                
        f.close()
        
        if student_count == 0:
            return 0
        return total_score / student_count
    except FileNotFoundError:
        return "FileNotFoundError"