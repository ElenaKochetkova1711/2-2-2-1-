S = input().strip()
T = input().strip()

if len(S) != len(T):
    print(-1)
else: 
    for shift in range(len(S)):
        match = True
        for i in range(len(S)):
            if S[(i - shift) % len(S)] != T[i]:
                match = False
                break
        
        if match:
            print(shift)
            break
    else:
        print(-1)
