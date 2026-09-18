from collections import Counter
import heapq

class Word:
    def __init__(self,word,freq):
        self.word = word
        self.freq = freq
    def __lt__(self,other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        heap = []

        for word,freq in count.items():
            heapq.heappush(heap,Word(word,freq))
            if len(heap) > k:
                heapq.heappop(heap)

        return [ heapq.heappop(heap).word for _ in range(len(heap)) ][::-1]
        
        
