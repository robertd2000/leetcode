# [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/description/)

Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

- `Solution(int[] nums)` Initializes the object with the integer array `nums`.
- `int[] reset()` Resets the array to its original configuration and returns it.
- `int[] shuffle()` Returns a random shuffling of the array.

## Example 1:

```

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

```

## Constraints:

- `1 <= nums.length <= 50`
- `-10^6 <= nums[i] <= 10^6`
- All the elements of `nums` are unique.
- At most `10^4` calls in total will be made to reset and shuffle.

## Code

```ts
class Solution {
  nums: number[];

  constructor(nums: number[]) {
    this.nums = nums;
  }

  reset(): number[] {
    return this.nums;
  }

  shuffle(): number[] {
    const shuffled = [...this.nums];
    const n = shuffled.length - 1;

    for (let i = n; i > 0; i--) {
      const temp = shuffled[i];
      const randomIndex = Math.floor(Math.random() * (i + 1));
      shuffled[i] = shuffled[randomIndex];
      shuffled[randomIndex] = temp;
    }

    return shuffled;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

```py

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = self.nums[::]
        n = len(shuffled) - 1

        for i in range(n, 0, -1):
            temp = shuffled[i]
            randomIdx = random.randint(0, i)

            shuffled[i] = shuffled[randomIdx]
            shuffled[randomIdx] = temp

        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

```

```java

class Solution {
    int[] nums;

    public Solution(int[] nums) {
        this.nums = nums;
    }

    public int[] reset() {
        return this.nums;
    }

    public int[] shuffle() {
        int[] shuffled = this.nums.clone();

        for (int i = shuffled.length - 1; i > 0; i--) {
            int temp = shuffled[i];
            int randomIdx = (int) Math.floor(Math.random() * (i + 1));

            shuffled[i] = shuffled[randomIdx];
            shuffled[randomIdx] = temp;
        }

        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */

```
