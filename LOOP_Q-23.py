rows=int(input("Enter Number Of Rows: "))
asscinum=65
for i in range(1,rows):
    for j in range(1,i+1):
        char=chr(asscinum)
        print(char,end=" ")
    asscinum+=1
    print(" ",end="\n")