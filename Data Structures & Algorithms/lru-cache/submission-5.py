class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))

        
