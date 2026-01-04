class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time complexity: O(n) for sliding window
        # Space complexity: O(1) for fixed number of variables
        max_val = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])

            max_val = max(max_val, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_val
