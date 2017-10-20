class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        # 别偷懒！不能用连等！！
        sheet_s, sheet_p = {}, {}
        res = []
        for i in p:
            if i not in sheet_p:
                sheet_p[i] = 1
            else:
                sheet_p[i] += 1
        left = i = 0
        while i < len(s):
            temp = s[i]
            if temp not in sheet_p:
                left = i = i + 1
                sheet_s = {}
                continue
            if temp not in sheet_s:
                sheet_s[temp] = 1
            else:
                sheet_s[temp] += 1
            # 检查刚添加的是否超限
            if sheet_s[temp] > sheet_p[temp]:
                count = 0
                # 删除最开始的元素，left前移，使不超限
                for j in s[left:i]:
                    sheet_s[j] -= 1
                    count += 1
                    if j == temp:
                        break
                left += count
            if i == left + len(p) - 1:
                res.append(left)
                sheet_s[s[left]] -= 1
                left += 1
            if left > len(s) - len(p):
                break
            i += 1
        return res
