class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Time complexity: O(n) for iterating through position and speed
        # Space complexity: O(n) for all elements in stack in worst case
        car = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in car:
            time = (target - p)/float(s)
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        