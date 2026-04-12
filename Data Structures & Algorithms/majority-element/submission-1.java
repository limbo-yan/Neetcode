class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int len = nums.length;
        for (int num : nums) {
            int val = map.getOrDefault(num, 0) + 1;
            if (val > len / 2) return num;
            map.put(num, val);
        }
        return -1;
    }
}