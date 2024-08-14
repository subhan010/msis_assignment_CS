# n=1
# print ("Question "+str(n))
# n=n+1

# print("hi")


# print ("Question "+str(n))
# n=n+1

# #print(hello)



# print ("Question "+str(n))
# n=n+1
# print("Hello world")



# print ("Question "+str(n))
# n=n+1
# st1="good day"
# print(st1)



# print ("Question "+str(n))
# n=n+1


# print ("Question "+str(n))
# n=n+1



# print ("Question "+str(n))
# n=n+1
# num1=int(input("Enter 1st number "))
# num2=int(input("Enter 2nd number "))

# print("Sum")
# print(num1+num2)
# print("Difference")
# print(num1-num2)

# print("Product")
# print(num1*num2)
# print("Quotient")
# print(num1/num2)

# print("Reminder")
# print(num1%num2)

# print("Power")
# print(num1**num2)





# print ("Question "+str(n))
# n=n+1

# print(type(num1))

# print ("Question "+str(n))
# n=n+1
# num='12'
# print(int(num))


# print ("Question "+str(n))
# n=n+1
# print(type(num1))
# print(type(num2))

# print ("Question "+str(n))
# n=n+1
# flonum=float(input("Enter float number"))
# print(round(flonum,2))


# print ("Question "+str(n))
# n=n+1
# print(flonum)

# print ("Question "+str(n))
# n=n+1
# print("String")
# n1="hi"
# print("Numeric")
# n2=20
# print(n2)
# print("Complex")
# print(complex(3,6))
# print("List")
# ls=["apple","ant","cat","bag"]
# print(ls, type(ls))
# print("Dictonary")
# dicto={
# 	"Roll 1":"abc",
# 	"Roll 2":"efg",
# 	"Roll 3":"hij"
# }
# print(dicto,type(dicto))
# print("Set")
# sett={"apple","samsung","htc"}
# print(sett,type(sett))
# print("Tuple")
# tuplee=("minicooper","gtr","supra")
# print(tuplee,type(tuplee))


n=0
print ("Question "+str(n))
n=n+1
greetings="Welcome to Python Programming"
count=0
for i in greetings:
	if i!=' ':
		count=count+1
print(count)

print ("Question "+str(n))
n=n+1
fname=input("Enter your first name ")
lname=input("Enter your last name ")
print(fname,lname,greetings)
print ("Question "+str(n))
n=n+1
print(fname," ",lname)


print ("Question "+str(n))
n=n+1
print(fname[0:3])


print ("Question "+str(n))
n=n+1
print(lname[-3:])

print ("Question "+str(n))
n=n+1
print(lname[3:])

print ("Question "+str(n))
n=n+1
print(lname[3:6])

print ("Question "+str(n))
n=n+1

lss=["uthamppam","kheer"]
print(lss," ",type(lss))
print ("Question "+str(n))
n=n+1

lss.append("pulao")
print(lss)
print ("Question "+str(n))
n=n+1
ess=["sambar","poha"]

lss.extend(ess)
print(lss)
print ("Question "+str(n))
n=n+1
print(len(lss))
print ("Question "+str(n))
n=n+1
print(lss[0:2])
print ("Question "+str(n))
n=n+1
print(lss[-1])

print ("Question "+str(n))
n=n+1
number = input("Enter a number: ")
x = int(number)%2 #it should be int not str
if x == 0:# need to add colon
    print("The number is Even.")
else: #add colon
    print("The number is Odd.")

print ("Question "+str(n))
n=n+1
c = input("Enter temperature in Centigrade: ")
f = 9*(int(c)/5) +32
print("Temperature in Fahrenheit is: ", f)

print ("Question "+str(n))
n=n+1
counte = int(input("Enter the count of numbers: "))
i = 0
sum= 0
for i in range(counte):
    x = int(input("Enter an integer: "))
    sum = sum + x
    avg = sum/counte

print("The average is: ", avg)

print ("Question "+str(n))
n=n+1
strri=input("enter string ")
lsp=["abp","gty"]
strri.append("ht")
lsp.append("ttp")
