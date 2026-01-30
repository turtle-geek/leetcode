class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) for left and right pointers
        # Space Complexity: O(1) for fixed number of variables
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # Add the difference between the current and max height
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                # Add the difference between the current and max height
                water += right_max - height[right]
        
        return water