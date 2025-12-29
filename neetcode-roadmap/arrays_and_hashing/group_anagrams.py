class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time Complexity: O(n*m) where n is the number of strings and m is len of longest string
        # Space complexity: O(n*m)
        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)

            if key not in res:
                res[key] = []
            res[key].append(s)
        
        return list(res.values())