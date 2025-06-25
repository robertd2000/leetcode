var isValidSudoku = function (board) {
  const map = {};

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === ".") continue;

      let num = board[i][j],
        x = Math.floor(i / 3),
        y = Math.floor(j / 3);

      let err =
        map["r" + i + num] || map["c" + j + num] || map["b" + x + y + num];

      if (err) return false;

      map["r" + i + num] = 1;
      map["c" + j + num] = 1;
      map["b" + x + y + num] = 1;
    }
  }

  return true;
};
