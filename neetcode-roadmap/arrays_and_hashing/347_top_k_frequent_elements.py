class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time Complexity: O(n) for iterating though list
        # Space Complexity: O(n) for list, dictionary, bucket
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_dict.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if(len(res) == k):
                    return res
        return res

