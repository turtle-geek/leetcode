class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(n) for iterating through temperatures
        # Space Complexity: O(n) for result array
        stack = []
        n = len(temperatures)
        res = [0]*n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res