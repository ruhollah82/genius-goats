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