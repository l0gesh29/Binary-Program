import string
def get_value(res):
    x=0
    s=sum([x+int(i) for i in res])
    while(s>9):
        s=get_value(list(str(s)))
    return s
n= input()
res=[]
alphabet=string.ascii_lowercase
alpha_list=list(alphabet)
for i in n:
    if(i.isupper()):
        i=i.lower()
    res.append(str(alpha_list.index(i)+1))
ans=get_value(res)
print(ans)
