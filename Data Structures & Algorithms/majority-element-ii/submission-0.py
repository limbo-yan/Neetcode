class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        head, tail, countH, countT = 0, 0, 0, 0
        
        for i in range(len(nums)):
            j = len(nums) - i - 1
            if countH == 0:
                head = nums[i]
            if (nums[i] == head):
                countH += 2
            else:
                countH -= 1

            if countT == 0:
                tail = nums[j]
            if (nums[j] == tail):
                countT += 2
            else: 
                countT -= 1
        res = []
        if countH > 0:
            res.append(head)
        if countT > 0 and head != tail:
            res.append(tail)
        
        return res


