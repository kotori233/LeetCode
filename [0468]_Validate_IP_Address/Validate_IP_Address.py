class Solution(object):

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(IP):
            IP = IP.split('.')
            if len(IP) != 4:
                return 'Neither'
            for each in IP:
                if not each or not each.isdigit():
                    return 'Neither'
                if (each[0] == '0' and len(each) > 1) or int(each) > 255:
                    return 'Neither'
            return 'IPv4'

        def isIPv6(IP):
            IP = IP.split(':')
            if len(IP) != 8:
                return 'Neither'
            for each in IP:
                if not 0 < len(each) < 5:
                    return 'Neither'
                for i in each:
                    if i not in '0123456789abcdefABCDEF':
                        return 'Neither'
            return 'IPv6'

        if '.' in IP:
            return isIPv4(IP)
        if ':' in IP:
            return isIPv6(IP)
        return 'Neither'
