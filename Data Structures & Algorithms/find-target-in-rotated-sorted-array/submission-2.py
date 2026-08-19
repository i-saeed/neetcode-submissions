class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        if nums[0] == target:
            return 0

        while left <= right:
            mid = (left + right) // 2

            # check if hte mid point is already the target
            if nums[mid] == target:
                return mid

            # meaning right side is unsorted
            if nums[mid] >= nums[right]:
                # check if it lies on the left side which is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                # meaning right side is sorted

                # check if it lies on the right side
                if nums[right] >= target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid

        return -1   