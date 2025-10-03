x=map(int ,input().split())
tar=input()
tar=int(tar)
l=list(x)
m=0
n=0
for i in range(len(l)):
    f=tar-l[i]
    m=i
    if f in l[i+1:]:
        n=l.index(f,i+1)
        break
print(m,n)