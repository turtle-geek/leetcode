class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time Complexity: O(n) where n is number of items in buckets
        # Space Complexity: O(n) total number of items stored in the buckets
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        k_freq = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                k_freq.append(n)
                if len(k_freq) == k:
                    return k_freq