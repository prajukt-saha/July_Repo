def LargeSmallSum(arr):
    if(len(arr)==3 or len(arr)<3):
        return 0
    else:
        
        odd=[arr[i] for i in range(1,len(arr), 2)]
        even=[arr[i] for i in range(0,len(arr), 2)]

    odd.sort()
    even.sort()
    return(odd[1]+even[len(even)-2])
arr=[3,5,6,7,8,90,34,32,14,45]
print(LargeSmallSum(arr))
