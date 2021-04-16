n = int(input())
l=[]
c=1
ans=0
for i in range(0,n):
    l.append(int(input()))
for i in l[::-1]:      
    if(i==1):
        ans+=c
        c=c*2
    else:
        c=c*2
print(ans)
    
