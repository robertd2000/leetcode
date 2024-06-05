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

```ts
function commonChars2(words: string[]): string[] {
  let last = count(words[0]);
  for (let i = 1; i < words.length; i++) {
    last = intersection(last, count(words[i]));
  }

  const result: string[] = [];
  for (let i = 0; i < 26; i++) {
    while (last[i] > 0) {
      result.push(String.fromCharCode(i + "a".charCodeAt(0)));
      last[i]--;
    }
  }

  return result;
}

function count(word: string): number[] {
  const frequency = Array(26).fill(0);
  for (let char of word) {
    frequency[char.charCodeAt(0) - "a".charCodeAt(0)]++;
  }
  return frequency;
}

function intersection(freq1: number[], freq2: number[]) {
  return freq1.map((f1, idx) => Math.min(f1, freq2[idx]));
}
```
