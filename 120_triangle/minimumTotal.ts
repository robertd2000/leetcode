function minimumTotal(triangle: number[][]): number {
  for (let r = triangle.length - 2; r >= 0; r--) {
    for (let l = 0; l <= r; l++) {
      triangle[r][l] += Math.min(triangle[r + 1][l], triangle[r + 1][l + 1]);
    }
  }

  return triangle[0][0];
}
