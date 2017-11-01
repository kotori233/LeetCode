class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m, left, right = 0, 0, len(height) - 1
        while left < right:
            a, b = height[left], height[right]
            m = max(m, min(a, b) * (right - left))
            if a < b:
                left += 1
            else:
                right -= 1
        return m
