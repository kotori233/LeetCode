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
                temp = [M[i + h][j + w] for h in (-1, 0, 1) for w in (-1, 0, 1)
                        if -1 < i + h < height and -1 < j + w < wide]
                ans.append(sum(temp) // len(temp))
            res.append(ans)
        return res
