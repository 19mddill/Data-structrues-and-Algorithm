import heapq
class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.heap = []
        self.push_order = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] = self.freq.get(val,0) + 1
        heapq.heappush(self.heap,(-self.freq[val],-self.push_order,val))
        self.push_order += 1

        

    def pop(self):
        """
        :rtype: int
        """
        freq,order,val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
