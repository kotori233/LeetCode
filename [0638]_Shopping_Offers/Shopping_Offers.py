class Solution(object):

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.sheet = {}

        def helper(need):
            if need in self.sheet:
                return self.sheet[need]
            self.sheet[need] = sum(p * n for p, n in zip(price, need))
            for sp in special:
                new = tuple(n - s for n, s in zip(need, sp))
                if min(new) < 0:
                    continue
                self.sheet[need] = min(self.sheet[need], helper(new) + sp[-1])
            return self.sheet[need]

        return helper(tuple(needs))
