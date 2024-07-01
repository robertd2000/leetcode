type Datum = {
  value: string;
  timestamp: number;
};

class TimeMap {
  data: Map<string, Datum[]>;

  constructor() {
    this.data = new Map<string, Datum[]>();
  }

  set(key: string, value: string, timestamp: number): void {
    const datum: Datum = { value, timestamp };
    const found = this.data.get(key);
    if (found) {
      found.push(datum);
    } else {
      this.data.set(key, [datum]);
    }
  }

  get(key: string, timestamp: number): string {
    const found = this.data.get(key);
    if (found === undefined) {
      return "";
    }

    const closestDatum = this.binarySearch(found, timestamp);
    if (closestDatum === -1) {
      return "";
    }

    return found[closestDatum].value;
  }

  binarySearch(datums: Datum[], target: number) {
    let left = 0;
    let right = datums.length - 1;

    while (left <= right) {
      const mid = Math.floor(left + (right - left) / 2);
      const { value: midV, timestamp: midT } = datums[mid];

      if (midT <= target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    if (right < 0) {
      return -1;
    }

    return right;
  }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
