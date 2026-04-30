class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        prefix = 0
        res = 0
        hashmap[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            res += hashmap[prefix-k]
            hashmap[prefix] += 1
        
        return res