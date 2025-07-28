a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
c = []

for i in range(len(a)):
    isDuplicate = False
    for j in range(len(b)):
        if a[i] == b[j]:
            isDuplicate = True
            break
    if not isDuplicate:
        c.append(a[i])
for i in range(len(b)):
    isDuplicate = False
    for j in range(len(a)):
        if b[i] == a[j]:
            isDuplicate = True
            break
    if not isDuplicate:
        c.append(b[i])

print("Non-duplicate elements:", c)
