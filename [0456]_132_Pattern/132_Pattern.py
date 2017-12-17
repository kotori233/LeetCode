class Solution(object):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # s3 当前第二大数
        s3 = float('-inf')
        # s2 当前最大
        s2 = []
        for i in nums[::-1]:
            if i < s3:
                return True
            # s2后移寻求满足条件集合(加入s2时均满足i<=s2)
            while s2 and i > s2[-1]:
                # s2[-1]为第二大数s3候选，更新s3
                s3 = s2.pop()
            # s2更新为当前满足条件最近值
            s2.append(i)
        return False
