from typing import List


class SnapshotArray:
    def __init__(self, length: int):
        self.arr = {i:{0:0} for i in range(length)}
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snapId] = val
        
    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.arr[index]:
            return self.arr[index][snap_id]
        else:
            snapIds = list(self.arr[index].keys())
            i = bisect.bisect_left(snapIds, snap_id) - 1
            return self.arr[index][snapIds[i]]

    
snapshotArr = SnapshotArray(1)
snapshotArr.set(0,15)
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.get(0,2))
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.get(0,0))