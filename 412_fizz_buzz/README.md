# [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/)

Given an integer n, return a string array answer (1-indexed) where:

- `answer[i] == "FizzBuzz"` if i is divisible by 3 and 5.
- `answer[i] == "Fizz"` if i is divisible by 3.
- `answer[i] == "Buzz"` if i is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

## Example 1:

```
Input: n = 3
Output: ["1","2","Fizz"]
```

## Example 2:

```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```

## Example 3:

```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

## Constraints:

- `1 <= n <= 104`

```py

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []

        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))

        return list

```
