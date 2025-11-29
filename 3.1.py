s = input().strip()

open_count = 0
remove_count = 0

for char in s:
    if char == '(':
        open_count += 1
    elif char == ')':
        if open_count > 0:
            open_count -= 1
        else:
            remove_count += 1

remove_count += open_count

print(remove_count)