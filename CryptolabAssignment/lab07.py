print("Question 1 Transpostion")

keyword="ANALYST"
plaintext="THECENTRALINTELLIGENCEAGENCY"

array=[['t']*(len(keyword)) for _ in range(int(len(plaintext)/(len(keyword)-1)))]
count=0
for i in range(len(array)):
    if count==len(plaintext):
        break
    for j in range(len(array[i])):
        if count==len(plaintext):
            break
        array[i][j]=plaintext[count]
        count=count+1

temkey=sorted(keyword)
print(temkey)
dic={}
cnt=0
nc = len(array[0])
for i in range(nc):
    str=""
    for j in range(len(array)):
        str=str+array[j][i]
        count=count+1
    if keyword[cnt] not in dic:
        dic[keyword[cnt]]=[]
    dic[keyword[cnt]].append(str)
    cnt=cnt+1
print(sorted(dic))

ans=""
for i in sorted(dic):
    for j in (dic[i]):
        ans=ans+j

print(ans)


print("Question 2 multicolumner")

keyword="ALPHA"

plaintext="HEYTHEREARETIGER"

array=[['']*(len(keyword)) for _ in range(int(len(plaintext)/(len(keyword)-1)))]
count=0
for i in range(len(array)):
    if count==len(plaintext):
        break
    for j in range(len(array[i])):
        if count==len(plaintext):
            break
        array[i][j]=plaintext[count]
        count=count+1


temkey=sorted(keyword)
print(temkey)
dic={}
cnt=0
nc = len(array[0])
for i in range(nc):
    str=""
    for j in range(len(array)):
        str=str+array[j][i]
        count=count+1
    if keyword[cnt] not in dic:
        dic[keyword[cnt]]=[]
    dic[keyword[cnt]].append(str)
    cnt=cnt+1


ans=""
for i in sorted(dic):
    for j in (dic[i]):
        ans=ans+j

print(array)
print(ans)


keyword="HITLER"

plaintext=ans

array=[['']*(len(keyword)) for _ in range(int(len(plaintext)/(len(keyword)-1)))]
count=0
for i in range(len(array)):
    if count==len(plaintext):
        break
    for j in range(len(array[i])):
        if count==len(plaintext):
            break
        array[i][j]=plaintext[count]
        count=count+1

temkey=sorted(keyword)
print(temkey)
dic={}
cnt=0
nc = len(array[0])
for i in range(nc):
    str=""
    for j in range(len(array)):
        str=str+array[j][i]
        count=count+1
    if keyword[cnt] not in dic:
        dic[keyword[cnt]]=[]
    dic[keyword[cnt]].append(str)
    cnt=cnt+1


ans=""
for i in sorted(dic):
    for j in (dic[i]):
        ans=ans+j

print(array)
print(ans)

print("Question 3")

keyword="AYUSH"
msg="GEEKSFORGEEKS"

keymix=""
count=0
for i in msg:
    if(count==len(keyword)):
        count=0
    
    keymix=keymix+keyword[count]
    count=count+1

count=0
ans=""
for i in msg:
    temp=ord(i)-65
    tpm=ord(keymix[count])-65
    tmp=temp+tpm
    
    if(tmp>25):
        tmp=tmp-26
    tmp=tmp+65
    ans=ans+chr(tmp)
    count=count+1

print(ans)
print(keymix)

print("Question 4")
enc="attack"
mat=[[2,3],
     [3,6]]


a=0
b=0
count=0

for i in enc:
    
    if(count>1):
        count=0
    for j in range(len(mat)):
        mat[j][count],j
    count=count+1

    

    












