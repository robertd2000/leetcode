function searchMatrix(matrix: number[][], target: number): boolean {
  const n = matrix.length;
  const m = matrix[0].length;
  let row = 0;
  let col = m - 1;

  while (row < n && col >= 0) {
    if (matrix[row][col] === target) {
      return true;
    }

    if (matrix[row][col] > target) {
      col--;
    } else {
      row++;
    }
  }

  return false;
}
