class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        l = 0
        r = n - 1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r-=1
        return res
        
