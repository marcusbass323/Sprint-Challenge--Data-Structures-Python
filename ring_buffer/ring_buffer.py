class RingBuffer:
    def __init__(self, capacity):
        self.size = capacity
        self.arr = [None] 
        self.top1 = -1
        self.top2 = self.size

    def append(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = item
            
    def get(self):
        if self.size is None:
            return None
        else:
            return self.arr