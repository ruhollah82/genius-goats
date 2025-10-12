n=int(input())
if n==0:print(0)
else:
 a=list(map(int,input().split()))
 s=sum(a)
 m=s/n
 c=0
 for i in a:
  if i>m:c+=1
 print(c)
