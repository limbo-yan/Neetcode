class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        while idx < n:
            if nums[idx] <= 0 or nums[idx] > n:
                idx += 1
                continue
            
            i = nums[idx] - 1
            if nums[idx] != nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                idx += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        