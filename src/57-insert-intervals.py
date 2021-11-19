from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        i=0
        while(i<=len(intervals)-1):
            if(i+1 <= len(intervals)-1 and ((intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1])
                or (intervals[i+1][0] >= intervals[i][0] and intervals[i+1][0] <= intervals[i][1]))):
                
                row = min(intervals[i][0], intervals[i+1][0])
                col = max(intervals[i][1], intervals[i+1][1])
                del intervals[i:i+2]
                intervals.insert(i, [row, col])
            else:
                i += 1
        
        return intervals
            
sol = Solution()
ans = sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(ans)