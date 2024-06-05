# [1002. Find Common Characters](https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05)

Given a string array `words`, return _an array of all characters that show up in all strings within the `words` (including duplicates)._ You may return the answer in any order.

## Example 1:

```
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
```

## Example 2:

```
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
```

## Constraints:

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

# Code

```ts
function commonChars(words: string[]): string[] {
  if (words.length === 1) {
    return words[0].split("");
  }

  const res = [];
  const chars = new Set(words[0]);

  chars.forEach((char) => {
    let freq = Infinity;

    words.forEach((word) => {
      let count = word.split("").filter((c) => c === char).length;
      freq = Math.min(freq, count);
    });

    for (let i = 0; i < freq; i++) {
      res.push(char);
    }
  });

  return res;
}
```
