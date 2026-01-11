class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity: O(n) for iterating through the array
        # Space Complexity: O(n) for case of last element in list being part of the pair
        num_dict = {}

        for i, num in enumerate(nums):
            search_val = target - num
            
            if search_val in num_dict:
                return [num_dict[search_val], i]

            num_dict[num] = i
        