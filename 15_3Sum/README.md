# [15. 3Sum](https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150)

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Example 1:

```

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

## Example 2:

```

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

## Example 3:

```

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

## Constraints:

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

# Code

```python

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                t = a + nums[l] + nums[r]
                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

```

```ts
function threeSum(nums: number[]): number[][] {
  const n = nums.length;
  nums.sort((a, b) => a - b);

  const res = [];

  for (let i = 0; i < n - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let l = i + 1;
    let r = n - 1;

    while (l < r) {
      let s = nums[i] + nums[l] + nums[r];

      if (s < 0) {
        l++;
      } else if (s > 0) {
        r--;
      } else {
        res.push([nums[i], nums[l], nums[r]]);

        while (l < r && nums[l] === nums[l + 1]) {
          l++;
        }

        while (l < r && nums[r] === nums[r - 1]) {
          r--;
        }

        l++;
        r--;
      }
    }
  }

  return res;
}
```

```go

func threeSum(nums []int) [][]int {
	var res [][]int
	n := len(nums)
	slices.Sort(nums)

	for i := 0; i < n-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, n-1

		for l < r {
			s := nums[i] + nums[l] + nums[r]

			if s > 0 {
				r--
			} else if s < 0 {
				l++
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})

				for l < r && nums[l] == nums[l+1] {
					l++
				}

				for l < r && nums[r] == nums[r-1] {
					r--
				}

				l++
				r--
			}
		}
	}

	return res
}

```

```cpp

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1;
            int r = n - 1;

            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];

                if (s < 0) l++;
                else if (s > 0) r--;
                else {
                    res.push_back({nums[i], nums[l], nums[r]});

                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;

                    l++;
                    r--;
                }
            }
        }

        return res;
    }
};

```
