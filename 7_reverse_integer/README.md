# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions)

Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Example 1:

```
Input: x = 123
Output: 321
```

## Example 2:

```
Input: x = -123
Output: -321
```

## Example 2:

```
Input: x = 120
Output: 21
```

## Constraints:

- `-231 <= x <= 231 - 1`

# Code

```python

class Solution:
    def reverse(self, x: int) -> int:
        xs = str(x)
        xs = xs[::-1]

        if xs[-1] == '-':
            xs = '-' + xs[:-1]

        res = int(xs)

        if res > pow(2, 31) - 1 or res < -pow(2, 31) - 1:
            return 0
        return res

```

```js
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let res = 0;

  if (x < 0) {
    res = parseInt(String(x).slice(1).split().reverse().join()) * -1;
  } else {
    res = parseInt(String(x).split().reverse().join());
  }

  if (res > Math.pow(2, 31) - 1 || res < -Math.pow(2, 31)) {
    return 0;
  }

  return res;
};
```

```js
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let isNegative = false;

  if (x < 0) {
    isNegative = true;
    x = -x;
  }

  let res = 0;

  while (x > 0) {
    let digit = x % 10;
    x = Math.floor(x / 10);

    if (
      res > Math.floor((2 ** 31 - 1) / 10) ||
      (res === Math.floor((2 ** 31 - 1) / 10) && digit > 7)
    ) {
      return 0;
    }

    res = res * 10 + digit;
  }

  return isNegative ? -res : res;
};
```
