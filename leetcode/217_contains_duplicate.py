class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for n in nums:
            if n not in mem:
                mem[n] = 0
            else:
                mem[n] += 1

        for n in nums:
            if mem[n] > 0:
                return True
        return False