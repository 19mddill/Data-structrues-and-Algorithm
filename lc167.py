class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s<target:
                left += 1
            elif s> target:
                right -= 1
            else:
                return [left+1,right+1]
      def twoSumHashUnsorted(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,n in enumerate(numbers):
            complement = target - n
            if complement in seen:
                return [seen[complement]+1,i+1]
            seen[n] = i
      
