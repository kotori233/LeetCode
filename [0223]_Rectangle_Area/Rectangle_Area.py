class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        two_sum = (C - A) * (D - B) + (G - E) * (H - F)
        if E > C or A > G or B > H or F > D:
            return two_sum
        cover = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return two_sum - cover
