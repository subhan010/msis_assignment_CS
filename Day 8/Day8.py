print("TO find multiplicate inverse of number with mod 26")
n =int (input("ENter the number"))
rg=0
if(n>26):
    rg=n
else:
    rg=26
count=0
for i in range(1,rg+1):
    if n%i==0 and 26%i==0:
        count=count+1
    if count>=2:
        break

if count>=2:
    print("Unable to find multiplicate inverse because is GCD greater than 2")
else:
    rg=rg+1
    ans=0
    while(True):
        if(rg%n==0):
            ans=rg/n
            break
        else: 
            rg=rg+26

            
        
        
    print("Multiplicative inverse is: ",int(ans))