class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int[] frequency = new int[nums.length + 1];

        for (int i : nums) {
            if (frequency[i] >= res.size()) {
                res.add(new ArrayList<>());
            }

            res.get(frequency[i]).add(i);
            frequency[i]++;
        }

        return res;
    }
}