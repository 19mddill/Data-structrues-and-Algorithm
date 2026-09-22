class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ranks = { n: i for i,n in enumerate(nums2)}
        res = list()
        last_index = len(nums2) - 1
        for n in nums1:
            next_index = ranks[n]
            while True:
                next_index += 1
                if next_index > last_index:
                    res.append(-1)
                    break
                x = nums2[next_index]
                if x > n:
                    res.append(x)
                    break
            
        return res
    def nextGreaterElementMonotonic(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                next_greater[stack.pop()] = n
            stack.append(n)

        while stack:
            next_greater[stack.pop()] = -1

        return [ next_greater[n] for n in nums1 ]
