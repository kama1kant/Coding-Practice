from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        que, ans, t = [], [], []
        for i in range(len(tasks)):
            t.append([tasks[i][0], tasks[i][1], i])
        tasks = sorted(t, key=lambda x: x[0])
        time = tasks[0][0]
        print(tasks)

        while len(tasks) > 0 or len(que) > 0:
            # print(tasks, ' = ', que, ' = ', time, ans)
            if len(tasks) > 0 and tasks[0][0] <= time:
                t = tasks.pop(0)
                heapq.heappush(que, [t[1], t[2]])
            elif len(que) > 0:
                q = heapq.heappop(que)
                time += q[0]
                ans.append(q[1])
            else:
                time = tasks[0][0]
        # print()
        # print(tasks, ' = ', que, ' = ', time, ans)
        return ans


sol = Solution()
print(sol.getOrder([[1,2],[2,4],[3,2],[4,1]]))
print(sol.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))
print(sol.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(sol.getOrder([[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]]))
print(sol.getOrder([[100,100],[1000000000,1000000000]]))
