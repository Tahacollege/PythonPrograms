num=int(input("Enter A Number: "))
a=-1
b=1
for i in range(num+1):
    c=a+b
    a=b
    b=c
    print (c, end=" ")
