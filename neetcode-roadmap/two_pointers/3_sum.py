class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n^2)
        # Space Complexity: O(n) for result list
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                
        return res