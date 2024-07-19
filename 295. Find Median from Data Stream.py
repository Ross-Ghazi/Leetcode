# https://www.youtube.com/watch?v=itmhHWaHupI&ab_channel=NeetCode
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small=[] # max heap
        self.large=[] # min heap
    def addNum(self, num: int) -> None:
        small=self.small
        large=self.large
        if num<=large[0]:
            heapq.heappush(small,-1*num)         
        else:
            heapq.heappush(large,num)   
        
        if len(small)-len(self.heapmin)>1:
            temp=-1*heapq.heappop(self.heapmax)
            heapq.heappush(self.heapmin,temp)                
        elif len(self.heapmin)-len(self.heapmax)>1:
            temp=-1*heapq.heappop(self.heapmin)
            heapq.heappush(self.heapmax,temp)
    def findMedian(self) -> float:    
        
        a=-1*self.heapmax[0]
        b=self.heapmin[0]
        if len(self.heapmax)==len(self.heapmin):
            return 0.5*(a+b)
        elif len(self.heapmax)>len(self.heapmin):
            return a
        else:
            return b


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
