class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < strs[0].length(); i ++) {
            for (int j = 1; j < strs.length; j ++) {
                String s = strs[j];
                if (i == s.length() || strs[0].charAt(i) != s.charAt(i)) return sb.toString();
            }
            sb.append(strs[0].charAt(i));
        }
        return sb.toString();
    }
}