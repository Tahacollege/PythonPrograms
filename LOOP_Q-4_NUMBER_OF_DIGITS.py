num=int(input("Enter A Number: "))
usernum=num
count=0
while(num>0):
    i=int(num%10)
    if(i>0):
        count+=1
    num=num/10
print("Number Of Digits In ",usernum," = ",count)
        