s1=input().lower()
s2=input().lower()
ans=0
n=min(len(s1),len(s2))
for i in range(0,n):   
    if(len(s1[i])>len(s2[i]) or len(s2[i])>len(s1[i])):
        break
    if(s1[i]==s2[i]):
        ans+=1
print(ans)
