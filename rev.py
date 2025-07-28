def transpose(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]

m = [[0,1,2],[3,4,5],[6,7,8]]
n=len(m)
transpose(m)
for i in range(n-1, -1, -1):
    for j in range(0, n):
        print(m[i][j], end=' ')
    print()