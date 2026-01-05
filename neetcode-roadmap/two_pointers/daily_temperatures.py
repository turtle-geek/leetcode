class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Time complexity: O(n) for temps in temperatures
        # Space complexity: O(n)
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([t, i])
            
        return res
        