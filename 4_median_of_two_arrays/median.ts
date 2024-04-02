function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const n = nums1.length;
  const m = nums2.length;

  let i = 0;
  let j = 0;

  const res: number[] = [];

  while (i < n && j < m) {
    if (nums1[i] < nums2[j]) {
      res.push(nums1[i]);
      i++;
    } else {
      res.push(nums2[j]);
      j++;
    }
  }

  while (i < n) {
    res.push(nums1[i]);
    i++;
  }

  while (j < m) {
    res.push(nums2[j]);
    j++;
  }

  const q = Math.floor(res.length / 2);

  if (res.length % 2 == 0) {
    return (res[q] + res[q - 1]) / 2;
  }

  return res[q];
}
