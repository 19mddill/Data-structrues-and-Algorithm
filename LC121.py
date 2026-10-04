class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [0]*n
        minp = [0]*n
        minp[0] = prices[0]
        for i in range(1,len(prices)):
            minp[i] = min(prices[i],minp[i-1])
            dp[i] = max(dp[i-1],prices[i]-minp[i-1])
        return dp[-1]
    def maxProfit(self, prices):
        minp = float('inf')
        best = 0
        for p in prices:
            minp = min(p,minp)
            best = max(best,p - minp)
        return best
    def maxProfit(self, prices):
        left = 0
        best = 0
        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
            else: best  = max(best, prices[right]-prices[left])
        return best
