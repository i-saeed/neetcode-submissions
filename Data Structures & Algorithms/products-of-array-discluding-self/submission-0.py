class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_positions = [i for i in range(len(nums)) if nums[i]==0]
        if len(zero_positions) > 1:
            return [0 for _ in range(len(nums))]
        total_product = 1
        for num in nums:
            if num != 0:
                total_product = total_product * num
        
        products = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            
            if i in zero_positions or len(zero_positions) == 0:
                if num == 0:
                    products[i] = total_product
                else:
                    products[i] = int(total_product / num)
        return products
        