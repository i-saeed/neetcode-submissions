class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Sums = []

        reference_idx = 0
        while reference_idx < len(nums) - 1:
            left_idx = reference_idx + 1
            right_idx = len(nums) - 1        
            current_reference = nums[reference_idx]
            if current_reference > 0:
                break

            while left_idx < right_idx:
                left_num = nums[left_idx]
                right_num = nums[right_idx]
                current_sum = current_reference + left_num + right_num

                if current_sum == 0:
                    Sums.append([current_reference, left_num, right_num])
                    left_idx += 1
                    right_idx -= 1
                    while not nums[left_idx] > left_num and left_idx < right_idx:
                        left_idx += 1

                elif current_sum < 0:
                    left_idx += 1
                else:
                    right_idx -= 1

            while nums[reference_idx] <= current_reference and reference_idx < len(nums) - 1:
                reference_idx += 1                    

        return Sums



        