/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  reverse(matrix);
  transpose(matrix);
}

function reverse(matrix: number[][]): void {
  let l = 0;
  let r = matrix.length - 1;

  while (l < r) {
    const temp = matrix[l];

    matrix[l] = matrix[r];
    matrix[r] = temp;

    l++;
    r--;
  }
}

function transpose(matrix: number[][]): void {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < i; j++) {
      const temp = matrix[i][j];

      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }
}
