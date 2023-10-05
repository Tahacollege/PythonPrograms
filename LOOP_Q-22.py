rows=int(input("Enter Number Of Rows: "))
k=0
for i in range(1,rows):
    for j in range (1,i+1):
        k+=1
        print(k,end=" ")
    print(" ",end="\n")