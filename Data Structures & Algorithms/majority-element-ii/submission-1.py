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
        cnt1 = cnt2 = 0
        for num in nums:
            if num == head:
                cnt1 += 1
            elif num == tail:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            res.append(head)
        if cnt2 > len(nums) // 3 and head != tail:
            res.append(tail)

        return res


