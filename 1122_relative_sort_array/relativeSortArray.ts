function relativeSortArray(arr1: number[], arr2: number[]): number[] {
  const count = new Array<number>(1001).fill(0);

  for (let i of arr1) {
    count[i]++;
  }

  let pos = 0;

  for (let i of arr2) {
    while (count[i] > 0) {
      arr1[pos] = i;
      count[i]--;
      pos++;
    }
  }

  for (let i = 0; i < count.length; i++) {
    while (count[i] > 0) {
      arr1[pos] = i;
      count[i]--;
      pos++;
    }
  }

  return arr1;
}
