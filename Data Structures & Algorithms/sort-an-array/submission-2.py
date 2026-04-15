class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            i = left - 1
            j = left
            pivot = nums[right]
            while j <= right:
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            return i
        
        def quickSort(nums, left, right):
            if right <= left:
                return nums

            idx = partition(nums, left, right)
            quickSort(nums, left, idx - 1)
            quickSort(nums, idx + 1, right)
            return nums
        
        return quickSort(nums, 0, len(nums) - 1)

