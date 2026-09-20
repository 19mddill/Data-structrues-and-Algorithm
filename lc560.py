from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        count = 0

        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1
        return count
        
