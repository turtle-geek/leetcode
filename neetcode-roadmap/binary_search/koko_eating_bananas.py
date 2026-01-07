class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        
        result = right
        
        while left <= right:
            k = (left + right) // 2
            
            # Calculate total hours needed at speed k
            total_hours = 0
            for p in piles:
                # Math ceiling: (p + k - 1) // k is equivalent to math.ceil(p / k)
                total_hours += (p + k - 1) // k
            
            if total_hours <= h:
                # Speed is okay, but maybe we can go slower?
                result = k
                right = k - 1
            else:
                # Too slow, need to increase speed
                left = k + 1
                
        return result