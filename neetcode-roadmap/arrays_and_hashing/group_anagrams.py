class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time Complexity: O(n*m) where n is the number of strings and m is len of longest string
        # Space complexity: O(n*m)
        ana_dict = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)

            if key not in ana_dict:
                ana_dict[key] = []
            ana_dict[key].append(s)
        
        return list(ana_dict.values())