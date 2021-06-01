n=input()
v=['a','e','i','o','u','A','E','I','O','U']
ans=""
start=0
c=0
for i in range(0,len(n)):
    if(n[i] in v):
        c+=1
        if(c%2!=0):
            for j in range(start,i+1):
                ans+=n[j]
            start=i+1
        else:
            temp=n[start:i+1]
            ans+=temp[::-1]
            start=i+1
if(start!=len(n)):
    for i in range(start,len(n)):
        ans+=n[i]
print(ans)
