class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Complexity: O(n) for iterating through nums
        # Space Complexity: O(n) for case of all unique elements
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False