class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums1)
        k = min(k, n * len(nums2))
        idx = [0 for i in range(n)]
        res = []
        for i in range(k):
            t, m = 0, float('inf')
            for j in range(n):
                try:
                    if nums1[j] + nums2[idx[j]] <= m:
                        t = j
                        m = nums1[j] + nums2[idx[j]]
                except IndexError:
                    pass
            res.append([nums1[t], nums2[idx[t]]])
            idx[t] += 1
        return res
