class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time Complexity: O(n) for iterating through the string
        # Space Complexity: O(n) for maximum size of stack
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # Checks returns true if the stack is empty false if it contains elements
        return not stack
