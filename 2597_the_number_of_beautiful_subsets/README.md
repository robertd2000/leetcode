# [2597. The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/description/?envType=daily-question&envId=2024-05-23)

You are given an array `nums` of positive integers and a positive integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to k.

Return _the number of **non-empty beautiful** subsets of the array `nums`._

A subset of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

## Example 1:

```

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

```

## Example 2:

```

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

```

## Constraints:

- `1 <= nums.length <= 20`
- `1 <= nums[i], k <= 1000`

# Code

```python

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = 1
        freq = defaultdict(collections.Counter)

        for x in nums:
            freq[x % k][x] += 1

        for fr in freq.values():
            s = sorted(fr.items())

            def f(i: int) -> int:
                if i == len(s):
                    return 1
                skip = f(i + 1)
                take = 2 ** s[i][1] - 1
                if i + 1 < len(s) and s[i + 1][0] - s[i][0] == k:
                    take *= f(i + 2)
                else:
                    take *= f(i + 1)
                return skip + take

            result *= f(0)

        return result - 1


```
