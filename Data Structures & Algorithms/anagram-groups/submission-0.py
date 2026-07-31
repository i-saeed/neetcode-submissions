from collections import defaultdict

def createHash(input_str: str) -> str:
    hash = defaultdict(int)
    for char in sorted(input_str):
        hash[char] += 1
    result = []
    for x, y in hash.items():
        result.append(x)
        result.append(str(y))
    return ",".join(result)
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        
        for a_str in strs:
            hash = createHash(a_str)
            groups[hash].append(a_str)

        return list(groups.values())




