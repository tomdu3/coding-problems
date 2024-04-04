class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        count = 0
        max_count = 0
        for ch in self.s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -=1
            max_count = max(count, max_count)
        return max_count
