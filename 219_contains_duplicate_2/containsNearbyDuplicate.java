class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int value = nums[i];
            if (hash.containsKey(value) && i - hash.get(value) <= k) {
                return true;
            }
            hash.put(value, i);
        }

        return false;
    }
}