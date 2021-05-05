def func(x):
    return (x and(not(x&(x-1))))
n=int(input())
l=[]
l1=[]
for i in range(0,n):
    l.append(input())
for i in l:
    a=1
    b=0
    for j in i[::-1]:
        if(j=='1'):
            b+=a
        a=a*2
    l1.append(b)
for i in l1:
    if(func(i)):
        print("true")
    else:
        print("false")
