class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash =  new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = target - nums[i];

            if (hash.containsKey(num) && hash.get(num) != i) {
                return new int[]{i, hash.get(num)};
            }

            hash.put(nums[i], i);
        }

        return new int[]{};
    }
}