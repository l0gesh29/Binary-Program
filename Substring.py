n=list(input().lower())
n1=list(input().lower())
c=[]
for i in n:
    c.append(n1.count(i))
print(min(c))
