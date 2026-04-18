class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int key : map.keySet()) {
            pq.add(new int[]{key, map.get(key)});
        }
        int[] res = new int[k];
        while (--k >= 0) {
            res[k] = pq.poll()[0];
        }
        return res;
    }
}
