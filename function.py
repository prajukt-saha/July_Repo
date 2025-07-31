def differenceofSum(n,m):
    sum1=0
    sum=0
    for i in range (1,m+1,1):
        if (i%n==0):
            sum1+=i;

        else:
            sum+=i
    print(sum1)
    print(sum)
    return(sum-sum1)

print(differenceofSum(4,20))