class Solution {
    public int[] sortArray(int[] nums) {
        int[] count = new int[100001];
        for (int num : nums) {
            count[num + 50000] ++;
        }
        int i = 0;
        for (int j = 0; j < count.length; j ++) {
            int c = count[j];
            while (c -- > 0) {
                nums[i ++] = j - 50000;
            }
        }
        return nums;
    }
}