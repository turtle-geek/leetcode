class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Time Complexity: O(nlogn) for sorting the list
        # Space Compleixty: O(n) for list of cars
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_fleet_time = 0.0

        for p, s in cars:
            time = float(target - p) / s
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time
        return fleets