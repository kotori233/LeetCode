class Solution(object):

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        sheet = {}
        for i in s:
            sheet[i] = sheet.get(i, 0) + 1
        words = ["zero", "two", "four", "six", "eight",
                 "one", "three", "five", "seven", "nine"]
        keys = ['z', 'w', 'u', 'x', 'g', 'o', 'r', 'f', 'v', 'e']
        nums = ['0', '2', '4', '6', '8', '1', '3', '5', '7', '9']
        res = []
        for i in range(10):
            count = sheet.get(keys[i], 0)
            if count:
                res.extend([nums[i]] * count)
                for j in words[i]:
                    sheet[j] -= count
        return ''.join(sorted(res))
