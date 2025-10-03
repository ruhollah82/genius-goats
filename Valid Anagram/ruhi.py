#https://neetcode.io/problems/is-anagram?list=neetcode150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dS={}
        dT={}

        for i in s:
            if i in dS:
                dS[i] +=1
            else:
                dS[i] =1  

        for i in t:
            if i in dT:
                dT[i] +=1
            else:
                dT[i] =1            

        return dS == dT


#solution fateme 1

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




#solution important
print(sorted(s)==sorted(t))
