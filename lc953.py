class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        rank = { char:i for i,char in enumerate(order)}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break #if this fires else is skipped
            else:
                if(len(w1)>len(w2)):
                    return False
        return True
                


        
