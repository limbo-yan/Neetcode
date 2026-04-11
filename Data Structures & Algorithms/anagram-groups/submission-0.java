class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            int[] arr = new int[26];
            for (char c : str.toCharArray()) {
                arr[c - 'a'] ++;
            }
            String s = Arrays.toString(arr);
            List<String> l = map.getOrDefault(s, new ArrayList<String>());
            l.add(str);
            map.put(s, l);
        }
        List<List<String>> res = new ArrayList<>();
        for (List<String> val : map.values()) {
            res.add(val);
        }
        return res;
    }
}
