function judgeSquareSum(c: number): boolean {
  let start = 0;
  let end = Math.floor(Math.sqrt(c));

  while (start <= end) {
    const powSum = Math.pow(start, 2) + Math.pow(end, 2);

    if (powSum === c) {
      return true;
    } else if (powSum < c) {
      start++;
    } else {
      end--;
    }
  }

  return false;
}
