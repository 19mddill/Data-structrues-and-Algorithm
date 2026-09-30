class Solution(object):
    def removeDuplicates(self, nums):
        dash_count = 0
        s = 0
        for f in range(1,len(nums)):
            if nums[f] == nums[s]:
                nums[f] = "_"
                dash_count += 1
            else:
                s = f
        s = 0
        for f in range(len(nums)):
            if nums[f] != '_':
                nums[f],nums[s] = nums[s],nums[f]
                s += 1

        return len(nums) - dash_count
            
            
        
