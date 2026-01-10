class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time Complexity: O(n) for iterating through string
        # Space Complexity: O(n) for case of all unique characters
        if len(s) != len(t):
            return False
        
        char_dict = {}
        
        for i in range(len(s)):
            char_dict[s[i]] = char_dict.get(s[i], 0) + 1
            char_dict[t[i]] = char_dict.get(t[i], 0) - 1
        
        for val in char_dict.values():
            if val != 0:
                return False
        return True