class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j, k, g = m - 1, n - 1, n + m - 1
        while j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                nums1[g] = nums1[j]
                j -= 1
                g -= 1
            else:
                nums1[g] = nums2[k]
                k -= 1
                g -= 1
        nums1[:k + 1] = nums2[:k + 1]
