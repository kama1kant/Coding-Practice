class TimeMap:
    
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = {}
        self.dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        values = list(self.dict[key].keys())
        i = bisect.bisect_right(values, timestamp)
        
        return self.dict[key][values[i-1]] if i > 0 else ''


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
print(timeMap.get("foo", 5))


# def get(self, key: str, timestamp: int) -> str:
#         values = sorted(list(self.dict[key].keys()))
#         l, r = 0, len(values)-1

#         if values[0] == timestamp:
#             return self.dict[key][values[0]]
#         elif values[0] > timestamp:
#             return ''
#         elif values[-1] <= timestamp:
#             return self.dict[key][values[-1]]

#         while l < r:
#             m = (l+r)//2
#             if values[m] == timestamp or (values[m] < timestamp and values[m+1] > timestamp):
#                 print(timestamp)
#                 return self.dict[key][values[m]]
#             if values[l] == timestamp:
#                 return self.dict[key][values[l]]
#             elif values[r] == timestamp:
#                 return self.dict[key][values[r]]

#             if values[m] > timestamp:
#                 r = m - 1
#             elif values[m] < timestamp:
#                 l = m + 1
#         print('here')
#         return self.dict[key][values[l]]
