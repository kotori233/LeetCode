class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(candidates, subres, target, last):
            if target == 0:
                self.res.append(subres[:])
            if target < candidates[0]:
                return
            for i in candidates:
                if i < last:
                    continue
                if i > target:
                    return
                subres.append(i)
                dfs(candidates, subres, target - i, i)
                subres.pop()

        if candidates == []:
            return self.res
        candidates.sort()
        dfs(candidates, [], target, 0)
        return self.res
