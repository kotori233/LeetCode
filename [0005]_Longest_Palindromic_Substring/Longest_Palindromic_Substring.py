class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.m, self.res = 0, ''

        def larger(left, right):
            count = right - left + 1
            while 1:
                left -= 1
                right += 1
                if left > -1 and right < len(s) and s[left] == s[right]:
                    count += 2
                else:
                    break
            if count > self.m:
                self.m = count
                self.res = s[left + 1:right]

        if len(s) < 2:
            return s
        for i in range(len(s)):
            larger(i, i)
            if i and s[i] == s[i - 1]:
                larger(i - 1, i)
        return self.res
