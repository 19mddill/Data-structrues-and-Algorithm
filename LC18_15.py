class Solution(object):
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
    
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.twoSum(nums, i, j, target - nums[i] - nums[j], result)
    
        return result
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.twosum(nums,i,result,-nums[i])
        return result
    def twosum(self,nums,i,result,target):
        L,R = i+1,len(nums)-1
        while L<R:
            s = nums[L] + nums[R]
            if target == s:
                result.append([-target,nums[L],nums[R]])
                while L<R and nums[L] == nums[L+1]: L += 1
                while L<R and nums[R] == nums[R-1]: R -= 1
                L += 1
                R -= 1
            elif s < target:
                L += 1
            else:
                R -= 1

        

        
