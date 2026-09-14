from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        seen = defaultdict(list)
        for s in strs:
            seen["".join(sorted(s))].append(s)
        return list(seen.values())
