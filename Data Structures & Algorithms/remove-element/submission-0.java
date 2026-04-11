class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0] == val ? 0 : 1;
        int pointer = nums.length - 1;
        for (int i = 0; i <= pointer; i ++) {
            if (nums[i] == val) {
                while (pointer >= i && nums[pointer] == val) pointer --;
                if (pointer < i) return Math.max(0, i);
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;                
            }
        }
        return nums.length;
    }
}