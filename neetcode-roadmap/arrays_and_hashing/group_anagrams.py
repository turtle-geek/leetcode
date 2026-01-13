class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time Complexity: O(n*m) where n is the number of strings and m is the length of longest string
        # Space Complexity: O(n*m) where n is the number of strings and m is length of longest character
        word_dict = {}
        for s in strs:
            key = 26*[0]
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key) # takes O(k) time where k is the number of characters in the alphabet
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(s)
        return list(word_dict.values())