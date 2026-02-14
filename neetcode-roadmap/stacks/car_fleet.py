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
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_fleet_time = 0.0

        for p, s in cars:
            time = float(target - p)/s
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time
        return fleets