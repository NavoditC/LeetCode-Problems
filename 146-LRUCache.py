from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            val = self.d[key]
            self.d.move_to_end(key,last=True)
            return val


    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.d.move_to_end(key,last=True)
        else:
            self.d[key] = value
        if len(self.d)>self.capacity:
            self.d.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
