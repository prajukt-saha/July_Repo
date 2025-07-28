key =5
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
k = key % n
rotated = arr[-k:] + arr[:-k]
print(rotated)