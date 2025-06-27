# [344. Reverse String](https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02)

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

## Example 1:

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

## Example 2:

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Constraints:

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ascii character.

```ts
/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    left++;
    right--;
  }
}
```

```cpp

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            swap(s[l], s[r]);
            l++;
            r--;
        }
    }
};

```
