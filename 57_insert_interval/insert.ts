function insert(intervals: number[][], newInterval: number[]): number[][] {
  const n = intervals.length;
  const res: number[][] = [];

  for (let i = 0; i < n; i++) {
    if (newInterval[1] < intervals[i][0]) {
      res.push(newInterval);
      return [...res, ...intervals.slice(i)];
    } else if (newInterval[0] > intervals[i][1]) {
      res.push(intervals[i]);
    } else {
      const start = Math.min(newInterval[0], intervals[i][0]);
      const end = Math.max(newInterval[1], intervals[i][1]);
      newInterval = [start, end];
    }
  }

  res.push(newInterval);

  return res;
}
