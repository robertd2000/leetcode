function maxDistToClosest(seats: number[]): number {
  const n = seats.length;

  let max = 0;
  let count = 0;
  let i = 0;

  if (seats[0] === 0) {
    while (seats[i] === 0) {
      count++;
      max = Math.max(max, count);
      i++;
    }
  }

  for (; i < n; i++) {
    if (seats[i] === 0) {
      count++;
      if (i === n - 1) {
        max = Math.max(max, count);
      } else {
        max = Math.max(max, Math.ceil(count / 2));
      }
    } else {
      count = 0;
    }
  }

  return max;
}
