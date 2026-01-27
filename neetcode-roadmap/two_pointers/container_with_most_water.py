class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time complexity: O(n) for two pointers
        # Space complexity: O(1) for fixed number of variables
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            h_l = height[l]
            h_r = height[r]

            if h_l < h_r:
                area = h_l * (r - l)
                l += 1
            else:
                area = h_r * (r - l)
                r -= 1
                
            max_area = max(max_area, area)

        return max_area
