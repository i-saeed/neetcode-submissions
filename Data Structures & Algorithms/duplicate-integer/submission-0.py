
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = dict()
        repeat = False
        for num in nums:
            if num not in container:
                container[num] = 1
            else:
                repeat = True
                break
        return repeat

        