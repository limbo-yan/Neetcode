class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n
        l = m - 1
        r = n - 1
        while idx > 0:
            idx -= 1
            if l < 0:
                nums1[idx] = nums2[r]
                r -= 1
                continue

            if nums1[l] > nums2[r]:
                nums1[idx] = nums1[l]
                l -= 1
            else:
                nums1[idx] = nums2[r]
                r -= 1
                if r < 0:
                    return
        
        