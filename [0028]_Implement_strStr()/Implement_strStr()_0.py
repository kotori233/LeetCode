class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        k, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        # 求解next数组，k前缀，j后缀
        while j < n - 1:
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                # 迭代next，向前寻找k中的更小前缀
                k = next[k]
        k = j = 0
        while k < m and j < n:
            if j == -1 or haystack[k] == needle[j]:
                k += 1
                j += 1
            else:
                j = next[j]
        if j == n:
            return k - j
        return -1
