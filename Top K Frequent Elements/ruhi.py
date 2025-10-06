from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        sorted_list = sorted(count.items() , key=lambda item : item[1],reverse=True)
        newlist = []
        for i in range(k):
            newlist.append(sorted_list[i][0])
        print(newlist)
        return newlist    
        
        