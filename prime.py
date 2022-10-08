a=int(input("enter the number"))
flag=False
if a>1:
    for i in range (2,a):
        if (a % i)==0:
            flag=True
            break
if flag:
    print("number is not prime")
else:
    print("number is prime")           
    
