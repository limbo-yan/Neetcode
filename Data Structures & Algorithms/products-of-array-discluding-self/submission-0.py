class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        hasZero = False
        for num in nums:
            if num == 0:
                if hasZero:
                    return [0]*(len(nums))
                hasZero = True
                continue
            total *= num 
        res = []
        for num in nums:
            if hasZero:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)
        return res
        