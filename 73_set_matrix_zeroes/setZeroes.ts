/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  const n = matrix.length;
  const m = matrix[0].length;

  let isCol = false;
  let isRow = false;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (matrix[i][j] === 0) {
        matrix[0][j] = 0;
        matrix[i][0] = 0;
        if (i === 0) {
          isCol = true;
        }
        if (j === 0) {
          isRow = true;
        }
      }
    }
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
      if (matrix[0][j] === 0 || matrix[i][0] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  if (isCol) {
    for (let i = 0; i < m; i++) {
      matrix[0][i] = 0;
    }
  }

  if (isRow) {
    for (let i = 0; i < n; i++) {
      matrix[i][0] = 0;
    }
  }
}
