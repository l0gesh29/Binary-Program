n= int(input())
name=[]
price=[]
weight=[]
res=0
for i in range(0,n):
    name.append(input())
for j in range(0,n):
    price.append(int(input()))
for k in range(0,n):
    weight.append(int(input()))
for i in range(0,n):
    a=0
    b=0
    c=0
    for j in range(i+1,n):
        if(name[i] == name[j]):
            a+=1
        if(weight[i] == weight[j]):
            b+=1
        if(price[i] == price[j]):
            c+=1
    if(a!=0 and b!=0 and c!=0):
        res+=1
print(res)
