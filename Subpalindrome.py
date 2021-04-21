n = input()
l=len(n)
list1=[]
count=0
for i in range(0,l):
    for j in range(i,l):
        list2=n[i:j+1]
        list1.append(list2)
for i in list1:
    if i==i[::-1]:
        count+=1
print(count)
