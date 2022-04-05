class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mem = {i: [] for i in range(numCourses)}
        q = [i for i in range(numCourses)]

        for [a, b] in prerequisites:
            if a in q:
                q.remove(a)
            mem[a].append(b)

        while q:
            c = q.pop(0)
            for ele in mem:
                if c in mem[ele]:
                    mem[ele].remove(c)
                    if not mem[ele]:
                        q.append(ele)

        for ele in mem:
            if mem[ele]:
                return False
        return True
