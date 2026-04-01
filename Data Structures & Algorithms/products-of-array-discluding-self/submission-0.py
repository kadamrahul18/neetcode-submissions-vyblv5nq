class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product_array[i] *= nums[j]
        return product_array