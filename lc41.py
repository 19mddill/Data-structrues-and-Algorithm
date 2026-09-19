import heapq
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set(nums)
        i = 1
        while True:
            if i not in seen:
                return i
            i += 1
            
        
