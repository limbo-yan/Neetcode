class Solution:
    def merge(self, res, l, m, r):
        left = res[l:m+1]
        right = res[m+1:r+1]

        idx = l
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res[idx] = left[i]
                i += 1
            else:
                res[idx] = right[j]
                j += 1
            idx += 1

        while j < len(right):
            res[idx] = right[j]
            j += 1
            idx += 1
        while i < len(left):
            res[idx] = left[i]
            i += 1
            idx += 1
        
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, left, right):
            if left == right:
                return arr
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)


