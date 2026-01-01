class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) for iterating through nums
        # Space Complexity: O(n) for creating set
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_streak +=1
                    current_num += 1
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
            