m=[[0,0,1],[0,0,0],[1,1,1]]
count=0
count_1=0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            count_1 += 1
        else:
            count += 1
if(count_1 > count):
    print("There are more 0s than 1s")  
    print("Number of 0s:", count_1)
else:
    print("There are more 1s than 0s")
    print("Number of 1s:", count)