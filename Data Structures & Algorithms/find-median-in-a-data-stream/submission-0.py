class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        if not self.minheap and not self.maxheap:
            heapq.heappush(self.minheap, num)
        elif self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        if abs(len(self.minheap) - len(self.maxheap)) > 1:
            popped = 0
            if len(self.minheap) > len(self.maxheap):
                popped = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -popped)
            else:
                popped = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -popped)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2.0