
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {num: idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            residual = target - num
            if residual in map and map[residual] != idx:
                return [idx, map[target-num]]
        
        return []
        