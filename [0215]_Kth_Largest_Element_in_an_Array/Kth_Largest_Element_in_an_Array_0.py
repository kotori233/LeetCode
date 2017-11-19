class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for i in nums:
            if i > pivot:
                nums1.append(i)
            elif i < pivot:
                nums2.append(i)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        temp = k - (len(nums) - len(nums2))
        if temp > 0:
            return self.findKthLargest(nums2, temp)
        return pivot
