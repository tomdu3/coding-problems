class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        count = 0
        mins = sorted([float(d) / s for d,s in zip(dist, speed)])

        for index, minute in enumerate(mins):
            if minute <= index:
                break
            count += 1
        return count