class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) for iterating through the set
        # Space Complexity: O(n) for storing the list elements
        if not nums:
            return 0

        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if (num - 1) not in num_set:
                search_val = num
                count = 1

                while search_val + 1 in num_set:
                    count += 1
                    search_val += 1
                max_count = max(max_count, count)
        
        return max_count
            