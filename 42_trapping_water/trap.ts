function trap(height: number[]): number {
  const n = height.length;

  let total = 0;

  let left = 1;
  let right = n - 2;

  let maxLeft = height[0];
  let maxRight = height[n - 1];

  while (left <= right) {
    if (maxLeft < maxRight) {
      maxLeft = Math.max(maxLeft, height[left]);
      total += maxLeft - height[left];
      left++;
    } else {
      maxRight = Math.max(maxRight, height[right]);
      total += maxRight - height[right];
      right--;
    }
  }

  return total;
}
