class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hi = max(arr)
        lo = min(arr)
        n = len(arr)

        if hi == lo:
            return True
        if (hi - lo)%(n-1) != 0:
            return False

        d = (hi - lo)//(n-1)
        
        seen = set(arr)

        for i in range(n):
            expected = lo + i * d
            if expected not in seen:
                return False
        return True
