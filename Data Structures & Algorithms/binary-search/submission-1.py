class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if target < nums[right]:
                right -= 1
            elif target > nums[left]:
                left += 1
            elif target == nums[left]:
                return left
            elif target == nums[right]:
                return right
        return -1