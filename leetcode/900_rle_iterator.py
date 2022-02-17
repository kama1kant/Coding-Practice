from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.c, self.n, self.i = [], [], 0
        for i in range(0, len(encoding), 2):
            if encoding[i] == 0:
                continue
            self.c.append(encoding[i])
            self.n.append(encoding[i+1])
        print(self.c, self.n)

    def next(self, n: int) -> int:
        while self.i < len(self.c):
            d = self.c[self.i] - n
            if d >= 0:
                self.c[self.i] = d
                print(self.c, self.n, self.i)
                return self.n[self.i]
            else:
                n = abs(d)
                self.i += 1
        return -1


rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5])
print(rLEIterator.next(2))
print(rLEIterator.next(1))
print(rLEIterator.next(1))
print(rLEIterator.next(2))