class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        pq = []
        for key, value in count.items():
            heapq.heappush(pq, (-value, key))
            # if len(pq) > k:
            #     heapq.heappop(pq)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
        