#https://neetcode.io/problems/duplicate-integer?list=neetcode150

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myList = []
        for i in nums:
            if i in myList:
                return True
            else:
                myList.append(i)

        return False
