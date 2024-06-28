function orangesRotting(grid: number[][]): number {
  const rowLength = grid.length;
  if (rowLength === 0) return -1;
  const colLength = grid[0].length;

  for (let row = 0; row < rowLength; row++) {
    for (let col = 0; col < colLength; col++) {
      if (grid[row][col] === 2) {
        rott(grid, row, col, 2);
      }
    }
  }
  let minutes = 2;

  for (let row = 0; row < rowLength; row++) {
    for (let col = 0; col < colLength; col++) {
      if (grid[row][col] === 1) {
        return -1;
      }
      minutes = Math.max(minutes, grid[row][col]);
    }
  }

  return minutes - 2;
}

function rott(grid: number[][], row: number, col: number, minutes: number) {
  const rowLength = grid.length;
  const colLength = grid[0].length;
  if (
    row < 0 ||
    row >= rowLength ||
    col < 0 ||
    col >= colLength ||
    grid[row][col] === 0 ||
    (grid[row][col] > 1 && grid[row][col] < minutes)
  ) {
    return;
  } else {
    grid[row][col] = minutes;
    rott(grid, row, col - 1, minutes + 1);
    rott(grid, row, col + 1, minutes + 1);
    rott(grid, row - 1, col, minutes + 1);
    rott(grid, row + 1, col, minutes + 1);
  }
}
