function maxArea(height: number[]): number {
  let l = 0;
  let r = height.length - 1;
  let max = 0;

  while (l < r) {
    const lH = height[l];
    const rH = height[r];
    let square = Math.min(lH, rH) * (r - l);

    if (square > max) {
      max = square;
    }

    if (lH < rH) {
      l += 1;
    } else {
      r -= 1;
    }
  }

  return max;
}
