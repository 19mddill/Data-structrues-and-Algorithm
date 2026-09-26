class Solution(object):
    def maxAreaBruteForce(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxv = 0
        for i in range(len(height)):
            L,R=0,len(height)-1
            current = height[i]
            while height[R] < current and i != R:
                R -= 1
            while height[L] < current and i != L:
                L += 1
            if (R - i) > (i - L):
                cv = (R - i) * height[i]
            else:
                cv = (i - L) * height[i]
            if cv > maxv:
                maxv = cv
        return maxv
      
      def maxArea(self, height):
        L = 0
        R = len(height)-1
        maxv = 0
        while L<R:
            maxv = max(maxv, min(height[L],height[R])*(R-L))
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return maxv

                

            
            

        
