class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        int n = nums.length / 2;

        for (int i : nums) {
            int value = hash.getOrDefault(i, 0) + 1;
            hash.put(i, value);
        }

        for (Map.Entry<Integer, Integer> entry : hash.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();

            if (value > n) {
                return key;
            }
        }

        return 0;
    }
}