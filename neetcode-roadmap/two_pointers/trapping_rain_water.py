class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            # We move the side that is lower because that side 
            # is the "bottleneck" for the water level
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # Water trapped is the difference between the max 
                # wall and the current floor
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water