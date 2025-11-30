n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = []

for i in range(n):
    found = False
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            result.append(j)
            found = True
            break
    
    if not found:
        result.append(-1)

print(' '.join(map(str, result)))