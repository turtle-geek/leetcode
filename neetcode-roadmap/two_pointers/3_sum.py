class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n^2) for iterating through the unique list values and secondary pointers
        # Space Complexity: O(n) for result list
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1
                
                else:
                    # total = 0
                    # -1,-1, 1,1,1,2,2
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == [l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return res