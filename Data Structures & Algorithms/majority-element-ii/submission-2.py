class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            res.append(cand1)
        if cnt2 > len(nums) // 3 and cand1 != cand2:
            res.append(cand2)

        return res


