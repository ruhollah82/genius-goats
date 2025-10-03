s=input()
t=input()
dic1={}
dic2={}
for i in s:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
    
for i in t:
    if i in dic2:
        dic2[i]+=1
    else:
        dic2[i]=1

print(dic1==dic2)




#solution 
print(sorted(s)==sorted(t))
