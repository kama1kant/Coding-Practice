class MovingAverage:
    
    def __init__(self, size: int):
        self.size = size
        self.bucket = []

    def next(self, val: int) -> float:
        self.bucket.append(val)
        if len(self.bucket) > self.size:
            self.bucket.pop(0)
        
        return sum(self.bucket)/len(self.bucket)