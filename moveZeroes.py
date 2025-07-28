arr = [1,2,3,4,5,0,6,7,8,0,2]
n = len(arr)
j = 0

for i in range(n):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1

for i in range(j, n):
    arr[i] = 0

for num in arr:
    print(num)
