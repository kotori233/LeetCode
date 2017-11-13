class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []

        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(s, subres):
            if s == '':
                self.res.append(subres)
            for i in range(len(s)):
                if not isPalindrome(s[:i + 1]):
                    continue
                dfs(s[i + 1:], subres + [s[:i + 1]])

        dfs(s, [])
        return self.res
