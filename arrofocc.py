arr = [10, 20, 10, 5, 20]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

result = []
seen = set()
for num in arr:
    if num not in seen:
        result.append([num, freq[num]])
        seen.add(num)

print(result)
