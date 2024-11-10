print("Question 1")
stri="Hello world"
j=-1
ans=""

for i in stri:
    ans=ans+stri[j]
    j=j-1

print(ans)
print("Question 2")
stro="aaabbbccc"
dic={}
for i in stro:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
ans2=""
for i in dic:
    ans2=ans2+i+str(dic[i])

print(ans2)

print("Question 3")
str3=input("Enter cesar cipher")
ansd=""
for i in str3:
    j=ord(i)
    j=j-3
    if((j<65 and j>=90) or  j<97 and j>=90):
        j=j+26
    ansd=ansd+chr(j)

print("Deciphered answer is ",ansd) 



print("Question 5")
str5=input("Enter plain text")
str6=input("Enter cipher text")

print("Key is ", ord(str6[0])-ord(str5[0]))


print("QUestion 6")
str7=input("Enter string")

anso=""
for i in str7:
    if(i.isupper()):
        temp=ord(i)-64
        temp=26-temp+1
        anso=anso+chr(temp+64)
    else:
        temp=ord(i)-96
        temp=26-temp+1
        anso=anso+chr(temp+96)
print(anso)

print("QUESTION 7")
print("affine encrypt")
enc="TWENTYFIFTEEN"
a=17
b=20
ans=""
for i in enc:
    tmp=ord(i)-65
    ans=ans+chr((((a*tmp)+b)%26)+65)
print(ans)

print("affine decrypt")
a=23
aan=""
for i in ans:
    tmp=ord(i)-65
    aan=aan+chr(((a*(tmp-b))%26)+65)

print(aan)
    

        

