from collections import defaultdict
import heapq


class Solution(object):

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sheet = defaultdict(list)
        for i in nums:
            pre = sheet[i - 1]
            t = heapq.heappop(pre) if pre else 0
            t += 1
            heapq.heappush(sheet[i], t)
        for each in sheet:
            for i in sheet[each]:
                if 0 < i < 3:
                    return False
        return True
