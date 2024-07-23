[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1
**Output:** [1]

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

```python

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for i, j in hashmap.items():
            frequency[j].append(i)

        res = []

        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res

        # hashmap = {}
        # res = []

        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1
        # print(hashmap)
        # sorted_hash = list(sorted(hashmap.items(), key=lambda item: item[1]))[::-1]
        # print(sorted_hash)

        # return [i for i, _ in list(sorted_hash)[:k]]

        # counter = Counter(nums).most_common(k)
        # return [i for i, _ in list(counter)]

```
