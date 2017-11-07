class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        ret = []
        for i in path:
            try:
                if i == '..':
                    ret.pop()
                elif i != '' and i != '.':
                    ret.append(i)
            except IndexError:
                ret = []
        return '/' + '/'.join(ret)
