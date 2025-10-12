n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    d[i]=1

c=0

for k in d:
 if k>0 and -k in d:
     c+=1

print(c)
