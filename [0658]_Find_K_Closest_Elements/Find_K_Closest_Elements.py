import bisect


class Solution(object):

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        count, n = 0, len(arr)
        left = max(bisect.bisect_right(arr, x) - 1, 0)
        start, end = left, left
        right = left + 1
        while count < k and (left > -1 or right < n):
            count += 1
            if right >= n or (left > -1 and x - arr[left] <= arr[right] - x):
                start = left
                left -= 1
            else:
                end = right
                right += 1
        return arr[start: end + 1]
