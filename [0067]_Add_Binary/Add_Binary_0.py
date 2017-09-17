class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ''
        j, k = len(a) - 1, len(b) - 1
        carry = 0
        while j >= 0 or k >= 0:
            if j >= 0:
                carry += int(a[j])
            if k >= 0:
                carry += int(b[k])
            ans = str(carry % 2) + ans
            carry = carry // 2
            j -= 1
            k -= 1
        if carry == 1:
            ans = '1' + ans
        return ans
