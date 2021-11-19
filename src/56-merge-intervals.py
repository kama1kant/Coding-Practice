from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        intervals.sort(key=lambda x: x[0])
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
ans = sol.merge([[1,4],[4,5]])
print(ans)