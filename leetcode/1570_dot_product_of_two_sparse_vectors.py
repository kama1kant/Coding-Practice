class SparseVector:
    def __init__(self, nums: List[int]):
        self.hash = {}
        for j, n in enumerate(nums):
            if n != 0:
                self.hash[j] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        prod, v1, v2 = 0, self.hash, vec.hash
        if len(self.hash.keys()) > len(vec.hash.keys()):
            v2, v1 = self.hash, vec.hash

        for j in v1:
            if j in v2:
                prod += v1[j] * v2[j]

        return prod
