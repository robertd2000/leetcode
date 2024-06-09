function uniquePaths(m: number, n: number): number {
  return helper(
    m,
    n,
    Array.from(Array(m + 1), () => new Array(n + 1))
  );
}

function helper(m: number, n: number, arr: number[][]): number {
  if (m == 1 && n == 1) return 1;
  if (m < 1 || n < 1) return 0;

  if (arr[m][n]) return arr[m][n];

  arr[m][n] = helper(m - 1, n, arr) + helper(m, n - 1, arr);

  return arr[m][n];
}
