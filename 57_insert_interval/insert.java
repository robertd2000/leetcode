class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) {
                result.add(interval);
            } else if (interval[0] > newInterval[1]) {
                result.add(newInterval);
                newInterval = interval;
            } else {
                int start = Math.min(interval[0], newInterval[0]);
                int end = Math.max(interval[1], newInterval[1]);
                newInterval = new int[] {start, end};
            }
        }

        result.add(newInterval);

        return result.toArray(new int[result.size()][]);
    }
}