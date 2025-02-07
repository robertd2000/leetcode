class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;
        if (n <= 1)
			return intervals;

		Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        Stack<int[]> res = new Stack<>();
        res.add(intervals[0]);

        for (int[] interval : intervals) {
            int[] prev = res.peek();

            if (prev[1] >= interval[0]) {
                prev[1] = Math.max(prev[1], interval[1]);
            } else {
                res.add(interval);
            }
        }
         
		return res.toArray(new int[res.size()][]);
    }   
}