h=int(input("Enter height: "))
for i in range (1,h+1):
    print(' '*(h-i)+str(i)*i, end='')
    print()