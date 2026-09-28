class Solution(object):
    def trap(self, height):

        L,R = 0, len(height)-1
        leftmax,rightmax = 0,0
        water = 0

        while L<R:
            if height[L] <= height[R]:
                if height[L] >= leftmax:
                    leftmax = height[L]
                else:
                    water += leftmax - height[L]
                L += 1
            else:
                if height[R] >= rightmax:
                    rightmax = height[R]
                else:
                    water += rightmax - height[R]
                R -= 1
        return water
        
