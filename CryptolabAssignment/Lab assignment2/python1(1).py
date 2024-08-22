import random
print("Question 1")
stri="helloworld"
print(len(stri))

print("Question 2")
print(stri[0:4])


print("Question 3")
sti2=" goodday"
print(stri+sti2)



print("Question 4")
print(sti2)
print(sti2.upper())

print("Question 5")
str3="CYBERSECURITY"
print(str3.lower())

print("Question 6")
ch='A'
print(ord(ch))

print("Question 7")
print(chr(67))

print("Question 8")
str4="Tommy world"
#print(str4.contain("wor"))

print("Question 9")

str5="hello how are you"

print(str5.replace('h','k'))


print("Question 10")
str6="hii"

print(str6.ljust(6,'x'))
print("Question 11")
str7="   hello world   "
print(str7)
print(str7.lstrip())
print(str7.rstrip())

print("Question 12")
str8="question8solution"
i=0
while i<(len(str8)):
    print(str8[i:(i+6)])
    i=i+6

print("Question 13")
str9="hellow world this is 913"
j=1
for i in str9:
    if i==' ':
        j=j+1
print("number of words",j)
print("Question 14")
fre={}
str10="Rocketrytest"
for i in str10:
    if i in fre:
        fre[i]=fre[i]+1
    else:
        fre[i]=1
print(fre)
print("Question 15")
#f=open("test89.txt","x")
#f.close()
print("Question 16")
f=open("test89.txt","r")
print("Question 17")
sty=f.read()
print(sty)


print("Question 18")
print(sty[::-1])

print("Question 19")
ty=len(str10)
for i in fre:
    fre[i]=round(((fre[i]/ty)*100),2)

print(fre)

print("Question 20")
io=int(input(" Enter number"))
print("modulo of 2 is:")
print(io%2)
print("Question 21")

print("Question 22")
ui=int(input("Enter the first number"))
uo=int(input("Enter the second number"))
temp=0
if(ui>uo):
    temp=uo
else:
    temp=ui
ans=0
for i in range(2,temp+1):
    if(ui%i==0 and uo%i==0):
        print("not co prime")
        ans=-1

if ans==0:
    print("Given numbers are coprime")

print("Question 23")
pu=int(input("Enter a number"))
print("Factors of number are: ")
for i in range (i,pu+1):
    if(pu%i==0):
        print(i)


print("Question 24")
print ("10 random numbers are")
for i in range (0,10):
    print(random.random())
print("Question 25")
print("Question 26")
