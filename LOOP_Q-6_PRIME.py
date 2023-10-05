num=int(input("Enter A Number; "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
if(prime):
    print("Number Is Prime");
else:
    print("Number Is Not Prime")