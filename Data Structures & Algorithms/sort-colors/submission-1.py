class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx0 = idx1 = 0
        for idx2 in range(len(nums)):
            num = nums[idx2]
            nums[idx2] = 2
            if num < 2:
                nums[idx1] = 1
                idx1 += 1
            if num < 1:
                nums[idx0] = 0
                idx0 += 1
            
