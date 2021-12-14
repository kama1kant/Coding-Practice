from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [0] * len(intervals)
        end = [0] * len(intervals)
        
        for i in range(len(intervals)):
            start[i] = intervals[i][0]
            end[i] = intervals[i][1]
        start.sort()
        end.sort()
        
        print(start)
        print(end)
        
        s_ptr = e_ptr = 0
        rooms = 0
        for i in range(len(intervals)):
            if start[s_ptr] >= end[e_ptr]:
                rooms -= 1
                e_ptr += 1
            
            rooms += 1
            s_ptr += 1
        
        return rooms
            
            
            

sol = Solution()
output = sol.minMeetingRooms([[13, 15], [1, 13]])
print(output)