from typing import List
import heapq

class StockPrice:
    def __init__(self):
        self.stock, self.latest, self.maxHeap, self.minHeap = {
        }, float(-inf), [], []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def update(self, timestamp: int, price: int) -> None:
        self.stock[timestamp] = price
        if timestamp > self.latest:
            self.latest = timestamp

        heapq.heappush(self.maxHeap, [-price, timestamp])
        heapq.heappush(self.minHeap, [price, timestamp])

    def current(self) -> int:
        return self.stock[self.latest]

    def maximum(self) -> int:
        while len(self.maxHeap) > 0:
            [p, t] = heapq.heappop(self.maxHeap)
            p *= -1
            if self.stock[t] == p:
                heapq.heappush(self.maxHeap, [-p, t])
                return p

    def minimum(self) -> int:
        while len(self.maxHeap) > 0:
            [p, t] = heapq.heappop(self.minHeap)
            if self.stock[t] == p:
                heapq.heappush(self.minHeap, [p, t])
                return p


stockPrice = StockPrice()
stockPrice.update(1, 10)
stockPrice.update(2, 5)
print(stockPrice.current())
print(stockPrice.maximum())
stockPrice.update(1, 3)
print(stockPrice.maximum())
stockPrice.update(4, 2)
print(stockPrice.minimum())