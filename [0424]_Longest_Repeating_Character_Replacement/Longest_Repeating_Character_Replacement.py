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
            maxCount = max(maxCount, sheet[s[right]])
            if right - left + 1 - maxCount > k:
                sheet[s[left]] -= 1
                left += 1
            else:
                res = max(res, right - left + 1)
        return res
