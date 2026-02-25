class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Left half is sorted properly
            if nums[left] <= nums[mid]:
                # Is the target within that sorted left half?
                if nums[left] <= target < nums[mid]:
                    # Narrow down search even more
                    right = mid - 1
                else:
                    # Ignore this half of the array from now on
                    left = mid + 1
            # Left half is not sorted correctly bleeding of larger values from the end
            # If the left half is not sorted correctly then the right half must be sorted right
            else:
                # Ignore the first half if the target is in the second half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Narrow down to first half
                else:
                    right = mid - 1
                    
        return -1