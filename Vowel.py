n= int(input())
l=[]
l1=[]
vowel=['a','e','i','o','u']
for i in range(0,n):
    l.append(input())
m= int(input())
for i in range(0,m):
    l1.append(list(input().split('-')))
for i in l1:
    c=0
    for j in range(int(i[0])-1,int(i[1])):
        if(l[j][0] in vowel and l[j][-1] in vowel):
            c+=1
    print(c)  
