class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        queue = [0]
        sheet = {}
        sheet[0] = 0
        while queue:
            pre = queue.pop(0)
            if pre == amount:
                return sheet[pre]
            for i in coins:
                temp = pre + i
                if temp > amount:
                    continue
                if temp not in sheet:
                    sheet[temp] = sheet[pre] + 1
                    queue.append(temp)
        return -1
