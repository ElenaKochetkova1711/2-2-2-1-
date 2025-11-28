def find_all_occurrences(text, pattern):
    
    if not pattern:
        return []
    
    def build_prefix_function(p):
        m = len(p)
        prefix = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and p[k] != p[i]:
                k = prefix[k - 1]
            if p[k] == p[i]:
                k += 1
            prefix[i] = k
        return prefix
    
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return []
    
    prefix = build_prefix_function(pattern)
    result = []
    j = 0  
    
    for i in range(n): 
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            result.append(i - m + 1)
            j = prefix[j - 1]
    
    return result

S = input().strip()
T = input().strip()

indices = find_all_occurrences(S, T)

print(' '.join(map(str, indices)))