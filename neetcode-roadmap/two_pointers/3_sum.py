class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n^2)
        # Space Complexity: O(n) for result set
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            seen = set()
            
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])
                
        return [list(t) for t in res]