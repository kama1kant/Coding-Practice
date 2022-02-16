class Logger:
    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict or timestamp >= self.dict[message]:
            self.dict[message] = timestamp+10
            return True
        else:
            return False


logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))
