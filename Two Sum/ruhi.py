#https://neetcode.io/problems/two-integer-sum?list=neetcode150

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            f = target - nums[i]  
            if f in nums[i+1:]:
                m = i
                n = nums.index(f, i+1)  
                break 
        return [m,n]