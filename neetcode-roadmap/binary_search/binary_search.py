class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Complexity: O(logn) for binary search
        # Space Complexity: O(1) for fixed number of variables
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1