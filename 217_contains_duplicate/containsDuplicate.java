class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<Integer>();

        for (int num : nums) {
            if (hashSet.contains(num)) {
                return true;
            }

            hashSet.add(num);
        }
        return false;
    }
}