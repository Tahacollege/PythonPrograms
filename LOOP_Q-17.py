a=int(input("enter the number: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print ("*",end=" ")
    print(" ",end="\n")
for k in range(a,0,-1):
    for j in range(k-1,0,-1):
        print("*",end=" ")
    print(" ",end="\n")