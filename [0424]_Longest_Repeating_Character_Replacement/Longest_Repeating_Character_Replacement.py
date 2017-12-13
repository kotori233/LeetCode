class Solution(object):

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '':
            return 0
        res, left, sheet, maxCount = 1, 0, {s[0]: 1}, 1
        for right in range(1, len(s)):
            sheet[s[right]] = sheet.get(s[right], 0) + 1
            # maxCount不更新，更新res无意义
            maxCount = max(maxCount, sheet[s[right]])
            # 杂草>k,左缩进
            # 虽然可能maxCount会变，但只会减小
            # 就算满足，窗口也小(直接忽略,继续右扩)
            if right - left + 1 - maxCount > k:
                sheet[s[left]] -= 1
                left += 1
            # 满足条件更新，不满足不更新(划重点！)
            else:
                res = max(res, right - left + 1)
        return res
