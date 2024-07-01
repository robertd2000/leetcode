[981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

**Example 1:**

**Input**
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
**Output**
[null, null, "bar", "bar", null, "bar2", "bar2"]

**Explanation**
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1); // return "bar"
timeMap.get("foo", 3); // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4); // return "bar2"
timeMap.get("foo", 5); // return "bar2"

**Constraints:**

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 107`
- All the timestamps `timestamp` of `set` are strictly increasing.
- At most `2 * 105` calls will be made to `set` and `get`.

```ts
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
```
