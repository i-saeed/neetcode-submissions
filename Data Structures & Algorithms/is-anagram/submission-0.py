from collections import defaultdict

def _listFreq(s: str) -> dict:
    freq = defaultdict(int)
    for occ in s:
        freq[occ] += 1
    return freq


class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreq = _listFreq(s)
        tFreq = _listFreq(t)
        return sFreq == tFreq
        

        