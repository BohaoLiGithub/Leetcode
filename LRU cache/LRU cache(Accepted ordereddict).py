class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remains = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.remains >= 1:
                self.remains -= 1
            else:
                self.cache.popitem(last = False)
        self.cache[key] = value