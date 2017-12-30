# You can type code here and execute it.

print("Hello World!")


class URLService(object):

    def __init__(self):
        self.long = {}
        self.short = {}
        self.idx = 1
        self.mask = \
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def convert(self, c):
        c = ord(c)
        if 47 < c < 58:
            return c - 48
        if 64 < c < 91:
            return c - 29
        if 96 < c < 123:
            return c - 87
        return -1

    def base62ToBase10(self, s):
        res = 0
        for i in s:
            res = res * 62 + self.convert(i)
        return res

    def base10ToBase62(self, n):
        res = ''
        while n:
            res = self.mask[n % 62] + res
            n //= 62
        while len(res) != 6:
            res = '0' + res
        return res

    def longToShort(self, url):
        shorturl = self.base10ToBase62(self.idx)
        self.long[self.idx] = url
        self.short[self.idx] = shorturl
        self.idx += 1
        return "http://tiny.url/" + shorturl

    def shortToLong(self, url):
        url = url[16:]
        idx = self.base62ToBase10(url)
        return self.long.get(idx, '')


if __name__ == '__main__':
    s = URLService()
    url = 'https://leetcode.com/problems/design-tinyurl'
    t = s.longToShort(url)
    print(t)
    print(s.shortToLong(t))
