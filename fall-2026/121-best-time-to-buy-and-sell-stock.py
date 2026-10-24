class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) access every element twice at most
        # Memory: O(1) pointers and ints are the only thing you store
        left = 0
        right = 0
        maxProfit = 0
        while right < len(prices):
            curProfit = prices[right] - prices[left]
            if curProfit > maxProfit:
                maxProfit = curProfit
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxProfit