class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        prev = 101
        for i in range(len(nums)):
            if nums[i] != prev:
                nums[idx] = nums[i]
                prev = nums[idx]
                idx += 1
        return idx