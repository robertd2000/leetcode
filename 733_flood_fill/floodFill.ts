function floodFill(
  image: number[][],
  sr: number,
  sc: number,
  color: number
): number[][] {
  const m = image.length;
  const n = image[0].length;

  const prevColor: number = image[sr][sc];

  if (prevColor === color) {
    return image;
  }

  function mark(sr: number, sc: number) {
    if (sr < 0 || sr >= m) return;
    if (sc < 0 || sc >= n) return;
    if (image[sr][sc] != prevColor) return;

    image[sr][sc] = color;

    mark(sr, sc - 1);
    mark(sr, sc + 1);
    mark(sr - 1, sc);
    mark(sr + 1, sc);
  }

  mark(sr, sc);

  return image;
}
