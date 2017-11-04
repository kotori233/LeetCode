class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(candidates, subres, target, i):
            if target == 0:
                self.res.append(subres[:])
                return
            while i < n:
                temp = target - candidates[i]
                if temp < 0:
                    return
                subres.append(candidates[i])
                dfs(candidates, subres, temp, i + 1)
                subres.pop()
                i += 1
                while i < n and candidates[i] == candidates[i - 1]:
                    i += 1

        candidates.sort()
        n = len(candidates)
        dfs(candidates, [], target, 0)
        return self.res
