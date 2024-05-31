class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int[] result = new int[] { 0, 0 };

        for (int i = 0; i < nums.length; i++) {
            int value = map.getOrDefault(nums[i], 0);
            map.put(nums[i], ++value);
        }
        int idx = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (value == 1 && idx < 2) {
                result[idx] = key;
                idx++;
            }
        }
        return result;
    }
}