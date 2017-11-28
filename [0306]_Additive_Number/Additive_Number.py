class Solution(object):

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def dfs(cur, count, pre2, pre1):
            if cur == n:
                return count > 3
            for size in range(1, n - cur + 1):
                if size > 1 and num[cur] == '0':
                    return False
                val = int(num[cur:cur + size])
                if count > 2 and val != pre1 + pre2:
                    continue
                if dfs(cur + size, count + 1, pre1, val):
                    return True
            return False

        n = len(num)
        return dfs(0, 1, None, None)
