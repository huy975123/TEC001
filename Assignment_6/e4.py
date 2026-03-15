def analyze_text(text):
    words = text.split()
    total_words = len(words)
    
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    lst = []
    for key, val in counts.items():
        lst.append((val, key))
        
    lst.sort(reverse=True)
    
    top_5 = dict()
    top_5_count = 0
    
    limit = 5
    if len(lst) < 5:
        limit = len(lst)
        
    for i in range(limit):
        val, key = lst[i]
        top_5[key] = val
        top_5_count = top_5_count + val
        
    print("Top 5:", top_5)
    print("Total number of words:", total_words)
    
    if total_words > 0:
        proportion = (top_5_count / total_words) * 100
        print("Proportion of 5 most common words:", top_5_count, "/", total_words, "=", str(proportion) + "%")

