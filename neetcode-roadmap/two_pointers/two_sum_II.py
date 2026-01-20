class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity: O(n) for left and right pointers moving through list
        # Space Complexity: O(1) for fixed number of variables
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l + 1, r + 1]