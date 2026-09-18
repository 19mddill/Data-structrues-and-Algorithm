from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = Counter(nums)
        result = 0
        for n in num_count.values():
            result += (n*(n-1))//2
        return result
        
