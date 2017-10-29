class Solution(object):

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        wide, height = len(M[0]), len(M)
        res = []
        for i in range(height):
            ans = []
            for j in range(wide):
                temp, count = M[i][j], 1
                if i != 0:
                    temp += M[i - 1][j]
                    count += 1
                    if j != 0:
                        temp += M[i - 1][j - 1]
                        count += 1
                if j != 0:
                    temp += M[i][j - 1]
                    count += 1
                    if i != height - 1:
                        temp += M[i + 1][j - 1]
                        count += 1
                if i != height - 1:
                    temp += M[i + 1][j]
                    count += 1
                    if j != wide - 1:
                        temp += M[i + 1][j + 1]
                        count += 1
                if j != wide - 1:
                    temp += M[i][j + 1]
                    count += 1
                    if i != 0:
                        temp += M[i - 1][j + 1]
                        count += 1
                ans.append(temp // count)
            res.append(ans)
        return res
