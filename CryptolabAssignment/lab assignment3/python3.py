import string
# print("Question 1")
# str1="Hellow world"
# ans0=""
# for i in str1:
#     if i.isupper():
#         temp=ord(i)-64
#         temp=(temp+3)%26
#         temp=temp+64
#         ans0=ans0+temp
#     else:
#         temp=ord(i)-96
#         temp=(temp+3)%26
#         temp=temp+96
#         ans0=ans0+temp
# print(ans0)

# print("Question 2")
# shift=int(input("ENter shift key"))
# str2="Hellow world"
# ans1=""
# for i in str2:
#     if i.isupper():
#         temp=ord(i)-64
#         temp=(temp+shift)%26
#         temp=temp+64
#         ans1=ans1+temp
#     else:
#         temp=ord(i)-96
#         temp=(temp+shift)%26
#         temp=temp+96
#         ans1=ans1+temp
# print(ans0)


# print("Question 3")
# str3="HELLO world this my place"
# print("the cipher text is ",str3)
# str3=str3.upper()
# count=0
# ans1=""
# temp=""

# for i in str3:
#     if i==' ':
#         continue
#     if count==5:
#         ans1=ans1+" "+temp
#         count=0
#         temp=i
#     else:
#         count=count+1
#         temp=temp+i
# if count>0:
#     ans1=ans1+" "+temp

# print(ans1)
    


# print("Question 4")
# file=open("file.txt","r")
# print(file.read())

# print("Question 5 and 6")
# file=open("file.txt","r")
# str3=file.read()
# print("Enctypting file content")

# ans2=""
# for i in str3:
#     if(i==' '):
#         ans2=ans2+' '
#         continue
#     if i.isupper():
#         temp=ord(i)-64
#         temp=(temp+3)%26
#         temp=temp+64
#         ans2=ans2+chr(temp)
#     else:
#         temp=ord(i)-96
#         temp=(temp+3)%26
#         temp=temp+96
#         ans2=ans2+chr(temp)
# print(ans2)





# print("Question 7")
# shift=int(input("ENter shift key"))
# str5=input("ENter the string")
# ans1=""
# for i in str5:
#     if i.isalpha()==0:
#         print("cant enrypt continas non alphabet letters")
#         ans1=""
#         break
  
#     if i.isupper():
#         temp=ord(i)-64
#         temp=(temp+shift)%26
#         temp=temp+64
#         ans1=ans1+chr(temp)
#     else:
#         temp=ord(i)-96
#         temp=(temp+shift)%26
#         temp=temp+96
#         ans1=ans1+chr(temp)
# print(ans1)

# print("Question 8")
# stre1="mug"
# stre2="gum"
# stre1=''.join(sorted(stre1))
# stre2=''.join(sorted(stre2))

# if(stre1==stre2):
#     print("Given strings are anagram")
# else:
#     print("GIven are not anagrams")



# print("Question 9")
# strr="RACECAR"
# anr=strr[::-1]
# if(strr==anr):
#     print("Is Palindrome")
# else:
#     print("Not palinedrome")


# print("Question 10")
# stry="Understand"
# strz="stand"
# flag=0
# for i in range(0,len(stry)):
#     if stry[i]==strz[0]:
#         for j in range(0,len(strz)):
#             if stry[i+j]==strz[j]:
#                 flag=1
#             else:
#                 flag=0
# if flag==1:
#     print("is substring")
# else:
#     print("not substring")



print("Question 11")
streein="Lorem isop !@# 87263TOMMY Vercettie"
low=""
upp=""
digit=""
pun=""

for i in streein:
    if i in string.ascii_lowercase:
        low=low+i
    if i in string.ascii_uppercase:
        upp=upp+i
    if i in string.digits:
        digit=digit+i
    if i in string.punctuation:
        pun=pun+i

print("Lower case ",low)
print("Upper case ",upp )
print("Digits case ",digit)
print("Punctions case ",pun)








