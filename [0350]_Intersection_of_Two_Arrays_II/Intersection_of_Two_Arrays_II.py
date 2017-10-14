class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sheet = {}
        res = []
        for i in nums1:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in nums2:
            if i in sheet and sheet[i] != 0:
                res.append(i)
                sheet[i] -= 1
        return res
