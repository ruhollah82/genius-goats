class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens :
            print(stk)
            sum = 0
            if i == "+":
                sum = stk.pop() + stk.pop()
                stk.append(sum)
                
            elif i == "*":
                sum = stk.pop() * stk.pop()
                stk.append(sum)
                
                
            elif i == "/":
                e= stk.pop()
                sum = stk.pop() / e
                stk.append(int(sum))
                
                
            elif i == "-":
                e= stk.pop()
                sum = stk.pop() - e
                stk.append(sum)
                
            else:
                stk.append(int(i))
        r = stk.pop()
        print(r)
        return int(r)     