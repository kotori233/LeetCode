class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq

        res = []
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 or n2 == 0:
            return res
        queue = [(nums1[0] + nums2[0], 0, 0)]
        while queue and len(res) < k:
            val, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < n1:
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
        return res
