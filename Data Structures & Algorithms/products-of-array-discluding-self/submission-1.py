class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        leftProd = [1] * size
        leftProd[0] = nums[0]

        rightProd = [1] * size
        rightProd[size-1] = nums[size-1]

        for i in range(1, size):
            j = size - 1 - i
            leftProd[i] = leftProd[i-1] * nums[i]
            rightProd[j] = rightProd[j+1] * nums[j]
        
        res = [1] * size
        res[0] = rightProd[1]
        res[size-1] = leftProd[size-2]
        for i in range(1, size-1):
            res[i] = leftProd[i-1] * rightProd[i+1]
        
        return res
