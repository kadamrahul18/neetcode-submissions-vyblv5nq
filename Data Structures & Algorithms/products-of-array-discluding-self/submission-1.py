class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        prefix[1], suffix[-2] = nums[0], nums[-1]
        product_array = [1] * n

        for i in range(n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        for i in range(n):
            product_array[i] = prefix[i - 1] * suffix[i + 1]
        
        return product_array

