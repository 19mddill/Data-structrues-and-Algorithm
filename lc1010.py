class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        seen = [0]*60 # index = remainder, value = frequency

        for t in time:
            A = t % 60
            if A == 0:
                B = 0
            else:
                B = 60 - A
            count += seen[B]
            seen[A] += 1

        return count

        
