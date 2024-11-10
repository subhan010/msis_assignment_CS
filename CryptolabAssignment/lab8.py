import random


print("Question 1")
a=12
b=13

while(True):
    temp=a%b
    if temp==0:
        break
    
    a=b
    b=temp
    
print("gcd ,",b)

if(b==1):
    print("they are co prime")
else :
    print("Not coprime")

print("Question 2")
def ext(a,b):
    if b==0:
        return a,1,0
    gcd, x1, y1=ext(b, a%b)
    x=y1
    y=x1 -(a//b) *y1
    return gcd, x, y

g, a, b=ext(3,11)

print(g,a,b)


print("Question 3")
bi="101011001010"
print("Golumb test 1")
z=0
o=0
flag=0
for i in bi:
    if i=='1':
        o=o+1
    else:
        z=z+1
if z>o:
    if z-o<=1:
        flag=1
else:
    if o-z<=1:
        flag=1

if flag==1:
    print("Golumb 1 test passed ")

if flag==1:
    dic={}
    count=1
    prev=-1
    for i in bi:
        
        if prev==-1:
            prev=i
            continue
        if prev==i:
            
            count=count+1
        else:
           
            if count in dic:
                dic[count]=dic[count]+1
            else:
                dic[count]=1
            
            count=1
        prev=i
    print(dic)    


print("Question 4")
l1=19807040628566084398385987584
l2=1267650600228229401496703205375
ii=random.randint(l1,l2)
print("generated random number is ",ii)
print("binary format is ",bin(ii))
tt=bin(ii)
dic={}
for i in range(len(tt)):
    for j in range(i+2,len(tt)):
        ttp=tt[i:j]
        
        if ttp not in dic:
            dic[ttp]=1
        else:
            dic[ttp]=dic[ttp]+1


for i in dic:
    if (dic[i]!=1):
        print(i)
        


