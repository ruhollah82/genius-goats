n,V=map(int,input().split())

a=list(map(int,input().split()))

d=[10**9]*(V+1)
d[0]=0
for i in range(1,V+1):
 for j in a:
  if i>=j:
   if d[i-j]+1<d[i]:
    d[i]=d[i-j]+1
if d[V]==10**9:
 print("Impossible")
else:
 print(d[V])
