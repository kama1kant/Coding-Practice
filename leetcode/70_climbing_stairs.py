class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 2]
        if n < 3:
            return mem[n-1]

        for i in range(2, n):
            mem.append(mem[i-1]+mem[i-2])

        return mem[n-1]
