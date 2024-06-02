function leastBricks(wall: number[][]): number {
  const intersections = {};

  for (let i = 0; i < wall.length; i++) {
    let brick = 0;
    for (let j = 0; j < wall[i].length - 1; j++) {
      brick += wall[i][j];
      if (brick in intersections) {
        intersections[brick]++;
      } else {
        intersections[brick] = 1;
      }
    }
  }

  let max = 0;

  for (let i in intersections) {
    if (intersections[i] > max) {
      max = intersections[i];
    }
  }

  return wall.length - max;
}
