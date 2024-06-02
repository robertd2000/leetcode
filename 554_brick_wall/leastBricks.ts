function leastBricks(wall: number[][]): number {
  const map = {};

  for (let i = 0; i < wall.length; i++) {
    let brick = 0;
    for (let j = 0; j < wall[i].length - 1; j++) {
      brick += wall[i][j];
      if (brick in map) {
        map[brick]++;
      } else {
        map[brick] = 1;
      }
    }
  }

  let max = 0;

  for (let i in map) {
    if (map[i] > max) {
      max = map[i];
    }
  }

  return wall.length - max;
}
