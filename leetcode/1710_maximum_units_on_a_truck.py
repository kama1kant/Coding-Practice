class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes, total = sorted(boxTypes, key=lambda x:x[1], reverse=True), 0
        
        for i, e in enumerate(boxTypes):
            if truckSize <= 0: break
            count = min(e[0], truckSize)
            truckSize -= count
            total += count * e[1]
        
        return total
        
sol = Solution()
print(sol.maximumUnits([[1,3],[2,2],[3,1]], 4))
print(sol.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))