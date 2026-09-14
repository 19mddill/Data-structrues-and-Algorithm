from collections import Counter,defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #return [ x for x,_ in Counter(nums).most_common(k)]
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        res = sorted(counter,key=counter.get,reverse=True)
        return res[:k]
