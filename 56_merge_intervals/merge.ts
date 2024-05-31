function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]);

  const results: number[][] = [intervals[0]];

  for (let interval of intervals) {
    const recent = results[results.length - 1];
    if (recent[1] >= interval[0]) {
      recent[1] = Math.max(recent[1], interval[1]);
    } else {
      results.push(interval);
    }
  }

  return results;
}
