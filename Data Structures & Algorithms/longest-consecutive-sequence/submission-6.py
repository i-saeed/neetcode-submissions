class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        residual = set(nums)

        current_stream = 0
        longest_streak = 1
        for res in residual:
            if res-1 not in residual:
                current_stream = 1
                while res + current_stream in residual:
                    current_stream += 1
                longest_streak = max(longest_streak, current_stream)

        
        return longest_streak
        


        