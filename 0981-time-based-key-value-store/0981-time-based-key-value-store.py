class TimeMap:

    def __init__(self):
        self.hashmap: dict[str, list[tuple[int, str]]] = {}
        # K: key, V: arr of tuple (timestamp, value), sorted in ascending order of timestamp
        # we use a list since want constant time access for binary search on `get`
        # since key.length is of fixed size, max number of buckets in hashmap is O(100 * 26) = O(1) 
        # timestamp is also of fixed length, so technically worst-case space complexity is O(100 * 26 * 10^7) = O(1)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # worst time complexity: O(n)
        # amoritzed time complexity: O(1)
        
        # strictly increasing `timestamp` will be used as args
        if key not in self.hashmap:
            self.hashmap[key] = []
            
        self.hashmap[key].append( (timestamp, value) )
        

    def get(self, key: str, timestamp: int) -> str:
        # worst time complexity: O(log n)
        vals = self.hashmap.get(key, [])
        
        # finds the position closest to the timestamp specified using binary search
        l, r = 0, len(vals) - 1
        last = ""
        
        while l <= r:
            m = l + (r - l) // 2
            
            if vals[m][0] < timestamp:
                last = vals[m][1]
                l = m + 1
            elif vals[m][0] > timestamp:
                r = m - 1
            else:
                return vals[m][1]
            
        return last
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)