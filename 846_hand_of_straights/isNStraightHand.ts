function isNStraightHand(hand: number[], groupSize: number): boolean {
  const n = hand.length;

  if (n % groupSize !== 0) return false;

  const map = {};

  for (let i of hand) {
    map[i] = map[i] ? map[i] + 1 : 1;
  }

  hand.sort((a, b) => a - b);

  for (let i of hand) {
    if (map[i] === 0) continue;

    for (let j = 0; j < groupSize; j++) {
      const curr = i + j;

      if (!map[curr]) {
        return false;
      }

      map[curr]--;
    }
  }

  return true;
}
