num=int(input("Enter The Number: "))
exponent=int(input("Enter The Power: "))
i=1
res=num
while(i<exponent):
    res=res*num
    i+=1
print(res)