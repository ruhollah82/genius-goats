class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s :
            if i == "(" or i == "{" or i == "[":
                stk.append(i)
            else:
                if len(stk) == 0 :
                    return False
                temp = stk.pop()
                if i == ")" and temp == "(":
                    continue
                if i == "]" and temp == "[":
                    continue
                if i == "}" and temp == "{":
                    continue
                return False
        if len(stk) == 0 :
            return True
        else:
            return False