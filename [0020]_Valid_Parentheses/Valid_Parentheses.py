class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        temp = ['']
        for each in s:
            if each in left:
                temp.append(each)
            else:
                key = (each == ')' and temp[-1] == '(') or (
                    each == ']' and temp[-1] == '[') or (each == '}' and temp[-1] == '{')
                if key:
                    temp.pop()
                else:
                    return False
        if temp != ['']:
            return False
        return True
