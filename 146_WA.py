class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.history = []

    def get(self, key: int) -> int:
        if str(key) in self.cache.keys():
            if str(key) in self.history:
                self.history.remove(str(key))
            self.history.append(str(key))
            return self.cache.get(str(key))
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity > 0:
            if str(key) in self.history:
                self.history.remove(str(key))
            self.history.append(str(key))
            self.cache.update({str(key):value})
            self.capacity = self.capacity - 1
        else:
            if str(key) in self.history:
                self.history.remove(str(key))
            else:
                del self.cache[self.history[0]]
                del self.history[0]
            self.history.append(str(key))
            self.cache.update({str(key):value})

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)