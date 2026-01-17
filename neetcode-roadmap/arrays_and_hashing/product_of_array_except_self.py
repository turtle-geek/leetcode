class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(n) for iterating through list
        # Space Complexity: O(n) for result list
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(n-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]

        return res

