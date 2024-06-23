# [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=daily-question&envId=2024-06-23)

Given an array of integers `nums` and an integer `limit`, return the size of the longest **non-empty** subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`_._

**Example 1:**

**Input:** nums = [8,2,4,7], limit = 4
**Output:** 2
**Explanation:** All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

**Example 2:**

**Input:** nums = [10,1,2,4,7,2], limit = 5
**Output:** 4
**Explanation:** The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

**Example 3:**

**Input:** nums = [4,2,2,2,4,4,2,2], limit = 0
**Output:** 3

**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
- `0 <= limit <= 109`

# Code

```python

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = collections.deque()
        incQ = collections.deque()
        ans = 0
        left = 0

        for right, num in enumerate(nums):
            while decQ and num > decQ[-1]:
                decQ.pop()

            decQ.append(num)

            while incQ and num < incQ[-1]:
                incQ.pop()

            incQ.append(num)

            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()

                if incQ[0] == nums[left]:
                    incQ.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans

```
