class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) one pass through the list
        # Memory: O(1) pointers and ints are the only thing you store
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                left = right
            right += 1
        return maxProfit