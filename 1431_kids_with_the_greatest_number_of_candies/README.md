# [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75)

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a _boolean array_ `result` of _length_ `n`, _where `result[i]` is true if, after giving the `ith` kid all the `extraCandies`, they will have the **greatest** number of candies among all the kids, or `false` otherwise_.

Note that **multiple** kids can have the **greatest** number of candies.

## Example 1:

```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

## Example 2:

```
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
```

## Example 3:

```
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

## Constraints:

- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_max = max(candies)
        res = []

        for i in candies:
            if i + extraCandies >= candies_max:
                res.append(True)
            else:
                res.append(False)

        return res

```

```go

func kidsWithCandies(candies []int, extraCandies int) []bool {
	res := []bool{}
	maxNum := max(candies)

	for _, i := range candies {
		if i+extraCandies >= maxNum {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}

	return res
}

func max(list []int) int {
	maxNum := 0

	for _, i := range list {
		if i > maxNum {
			maxNum = i
		}
	}

	return maxNum
}

```

```cpp

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;

        int max = findMax(candies);

        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= max) {
                result.push_back(true);
            } else {
                result.push_back(false);
            }
        }

        return result;
    }

    int findMax(vector<int>& list) {
        int max = 0;

        for (int i = 0; i < list.size(); i++) {
            if (list[i] > max) {
                max = list[i];
            }
        }

        return max;
    }
};

```
