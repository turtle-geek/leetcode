class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, n in enumerate(nums):
            lookup = target - n
            if lookup in hashMap:
                return [i, hashMap[lookup]]
            else:
                hashMap[n] = i
        return []