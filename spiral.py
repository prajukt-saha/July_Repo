rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
top = 0; bottom = rows - 1
left = 0; right = cols - 1

print("Input matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))
while (top <= bottom and left <= right):

    for i in range(left, right + 1):
        print(matrix[top][i], end=' ')
    top += 1

    for i in range(top, bottom + 1):
        print(matrix[i][right], end=' ')
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=' ')
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=' ')
        left += 1ght:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=' ')
        left += 1