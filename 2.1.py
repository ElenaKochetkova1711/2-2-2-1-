S = input().strip()
T = input().strip()

if not T:
    print("")
else:
    result = []
    start = 0
    
    while True:
        pos = S.find(T, start)
        
        if pos == -1:
            break
            
        result.append(pos)
        
        start = pos + 1
    
    print(' '.join(map(str, result)))
