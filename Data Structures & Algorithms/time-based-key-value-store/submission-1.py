class TimeMap:

    def __init__(self):
        self.dictMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """

        {
         alice: [ [sad, 1], 
        }

        """
        key_map = self.dictMap.get(key,[])
        res = ""
        l,r = 0, len(key_map) - 1
        while l <= r:
            mid = (l+r) // 2
            if key_map[mid][1] <= timestamp:
                res = key_map[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        
