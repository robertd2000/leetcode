# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

1. **Whitespace**: Ignore any leading whitespace (`" "`).
2. **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. **Rounding**: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

Return the integer as the final result.

## Example 1:

```
Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
```

## Example 2:

```
Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
```

## Example 3:

```
Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
```

## Example 4:

```
Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
```

## Example 5:

```
Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.
```

## Constraints:

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (0-9), `' '`, `'+'`, `'-'`, and `'.'`.

```ts
function myAtoi(s: string): number {
  let i = 0;
  const n = s.length;
  let res = 0;
  let sign = 1;

  while (i < n && s[i] === " ") i++;

  if (i < n && (s[i] === "-" || s[i] === "+")) {
    if (s[i] === "-") sign = -1;
    if (s[i] === "+") sign = 1;
    i++;
  }

  while (i < n && s[i] >= "0" && s[i] <= "9") {
    res = res * 10 + (s[i].charCodeAt(0) - "0".charCodeAt(0));
    if (res * sign > 2 ** 31 - 1) return 2 ** 31 - 1;
    if (res * sign < -(2 ** 31)) return -(2 ** 31);
    i++;
  }

  return res * sign;
}
```

```py

class Solution:
    def myAtoi(self, s: str) -> int:

        is_negative = False
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        res = ""

        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "+":
                is_negative = False
            elif s[i] == "-":
                is_negative = True
            i += 1

        while i < n and s[i] == "0":
            i += 1

        while i < n and s[i].isnumeric():
            res += s[i]
            i += 1

        if res == "":
            return 0

        m = int(res)

        if is_negative:
            m = -m

        if m > 0 and m >= INT_MAX:
            return INT_MAX

        if m < 0 and m <= INT_MIN:
            return INT_MIN

        return m


```

```js
var myAtoi = function (s) {
  let i = 0,
    n = s.length,
    sign = 1,
    result = 0;

  while (i < n && s[i] === " ") i++;

  if (i < n && (s[i] === "+" || s[i] === "-")) {
    sign = s[i] === "-" ? -1 : 1;
    i++;
  }

  while (i < n && s[i] >= "0" && s[i] <= "9") {
    result = result * 10 + (s[i].charCodeAt(0) - "0".charCodeAt(0));
    if (result * sign > 2 ** 31 - 1) return 2 ** 31 - 1;
    if (result * sign < -(2 ** 31)) return -(2 ** 31);
    i++;
  }

  return result * sign;
};
```

```go

var digits = map[byte]int{
	0x30: 0,
	0x31: 1,
	0x32: 2,
	0x33: 3,
	0x34: 4,
	0x35: 5,
	0x36: 6,
	0x37: 7,
	0x38: 8,
	0x39: 9,
}

func myAtoi(str string) int {
	res, sign, len, idx := 0, 1, len(str), 0

	// Skip leading spaces
	for idx < len && (str[idx] == ' ' || str[idx] == '\t') {
		idx++
	}

	if idx == len {
		return 0
	}

	// +/- Sign
	if str[idx] == '+' {
		sign = 1
		idx++
	} else if str[idx] == '-' {
		sign = -1
		idx++
	}

	// Digits: 0x30 = '0', 0x31 = '1', ... 0x39 = '9'
	for idx < len && str[idx] >= 0x30 && str[idx] <= 0x39 {
		res = res*10 + digits[str[idx]]
		if sign*res > math.MaxInt32 {
			return math.MaxInt32
		}

		if sign*res < math.MinInt32 {
			return math.MinInt32
		}

		idx++
	}

	return res * sign
}

```
