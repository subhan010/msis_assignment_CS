print("QUestion 1")
enc="dvvkzecfssprkkve"

for i in range(1,27):
    temp=""
    for j in enc:
        j=ord(j)-96
        j=j-i
        if j<=0:
            j=26+j
        j=j+96
        temp=temp+chr(j)
    
    print(temp)
    
print ("Decipher after brute force is meetinlobbyatten")

print("QUestion 2")
P="AB"
C="GL"
a=5
b=6
enc="XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS"

aan=""
for i in enc:
    tmp=ord(i)-65
    aan=aan+chr(((a*(tmp-b))%26)+65)

print(aan)
    
   

import math


print("Question 3")

key=3
qus="FLY-FOR-WE-ARE-DISCOVERED"
ans=""
dic={}

for i in range(3):
    dic[i]=""

print(dic)

cur=0
flag=0
for i in qus:
    dic[cur]=dic[cur]+i
    
    if flag==0:
        cur=cur+1
    else:
        cur=cur-1
    if cur>=key:
        cur=key-2
        flag=1
    elif cur==0:
        cur=0
        flag=0

ans=""
for i in dic:
    ans=ans+dic[i] 
print(ans)




# print("QUestion 4")

# key=3
# qus="FFWRIVDL-O-EAEDSOEEYR--CR"
# ans=""
# dic={}
# for i in range(3):
#     dic[i]=""
# k=2*(key-1)
# l=math.ceil(len(qus)/k)
# print(l)
# dic[0]=qus[0:l]
# print(dic[0])
# dic[key-1]=qus[-(l-1):]
# print(dic[key-1])
# cur=0
# flag=0
# tkey=0
# count=0
# ttm=key-2
# lenm=len(qus)-(2*l)-1

# io=1
# for l in range(ttm):



# for i in qus:

#     if cur==tkey:
#         dic[cur]=dic[cur]+i
#     if flag==0:
#         cur=cur+1
#     else:
#         cur=cur-1
#     if cur>=key:
#         cur=key-2
#         flag=1
#     elif cur==0:
#         cur=0
#         flag=0
#     if count==len(qus):
#         tkey=tkey+1
#     count=count+1

# ans=""
# for i in dic:
#     ans=ans+dic[i] 
# print(ans)


print("Question 4")
qus="AAIUJ SIHBE KTEAO TEADE SNUTF EAEMR TAHSA\
RHROA YHNFO AITTE EHCBO FVCAT RNMNS NUTFE\
RASHL WFHLN HIUJS IHTKS OEHNI FISAE FNTIG\
RMRSO LSTIS OKIEH PEOE"
enc=""
for i in qus:
    if(i==' '):
        continue
    enc=enc+i

l=len(enc)

s1=enc[0:int(l/2)]
s2=enc[int(l/2):]
ans=""
for i in range(int(l/2)):
    ans=ans+s1[i]+s2[i]

print(ans)
    

            
            
        
    
    
                    

        


        
        



    
    
    