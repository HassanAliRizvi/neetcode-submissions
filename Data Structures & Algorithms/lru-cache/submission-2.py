class LRUCache:

    
    def __init__(self, capacity: int):
        #missed writing self.capacity = capacity to be used in other classes
        self.capacity = capacity
        self.LRU_cache = {}
        
    def get(self, key: int) -> int:
        if key in self.LRU_cache:
            # missed doing pop then putting value back to most recent
            value = self.LRU_cache.pop(key)
            # this was done but NOT returned!
            self.LRU_cache[key] = value
            return value
        else:
            return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRU_cache:
            self.LRU_cache.pop(key)
        
        self.LRU_cache[key] = value
        
        if len(self.LRU_cache) > self.capacity:
            self.LRU_cache.pop(next(iter(self.LRU_cache)))
        
