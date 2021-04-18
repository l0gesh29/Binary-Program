def get_value(n):
    s=sum([int(x)**2 for x in n])
    while(s>9):
        s=get_value(list(str(s)))
    return s
n = input()
n=list(n)
ans=get_value(n)
print(ans)
