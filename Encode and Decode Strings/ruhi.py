class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) +"#"+i
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i =0
        l = ""
        temp = ""
        while i<len(s):
            if s[i] != "#":
                l = l + s[i] 
                i+=1
            else:
                l = int(l)   
                i+=1
                temp = s[i:i+l]
                decoded.append(temp)
                i = i+l
        print(decoded) 
        return(decoded)  
                 
            

                
                
            
            
            
            
                
                
            
            