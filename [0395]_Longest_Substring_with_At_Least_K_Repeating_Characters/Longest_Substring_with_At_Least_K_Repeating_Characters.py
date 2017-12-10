class Solution(object):

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if n < k:
            return 0
        # find the block
        sheet, block = {}, set()
        for c in s:
            sheet[c] = sheet.get(c, 0) + 1
            if sheet[c] < k:
                block.add(c)
            else:
                block.discard(c)
        if len(block) == 0:
            return n
        # divide
        i, divided = 0, []
        while i < n:
            if s[i] in block:
                i += 1
            else:
                start = i
                while i < n:
                    if s[i] not in block:
                        i += 1
                    else:
                        break
                divided.append((start, i))
        # conquer
        res = 0
        for each in divided:
            res = max(res, self.longestSubstring(s[each[0]:each[1]], k))
        return res
