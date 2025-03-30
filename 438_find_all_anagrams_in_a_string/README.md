# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

## Example 1:

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

## Example 2:

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Constraints:

- 1 <= s.length, p.length <= 3 \* 104
- s and p consist of lowercase English letters.

# Code

```py
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        for ch in p: hm[ch] += 1

        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1

        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm:
                hm[s[i+pL]] -= 1

            if all(v == 0 for v in hm.values()):
                res.append(i+1)

        return res

```

```py

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        for i in range(n - m + 1):
            if self.isAnagram(s[i : i + m], p):
                res.append(i)

        return res

    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for i in s:
            val = hmap.get(i, 0) + 1
            hmap[i] = val

        for i in t:
            val = hmap.get(i, 0) - 1
            hmap[i] = val

            if val < 0:
                return False

        for i in hmap.values():
            if i > 0:
                return False

        return True


```

```java

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();

        int n = s.length();
        int m = p.length();

        if (n < m)
            return res;

        int[] freqS = new int[26];
        int[] freqP = new int[26];

        for (int i = 0; i < m; i++) {
            int cs = s.charAt(i) - 'a';
            int cp = p.charAt(i) - 'a';
            freqS[cs]++;
            freqP[cp]++;
        }

        int start = 0;
        int end = m;

        if (Arrays.equals(freqS, freqP))
            res.add(start);

        while (end < n) {
            int cs = s.charAt(start) - 'a';
            int cp = s.charAt(end) - 'a';
            freqS[cs]--;
            freqS[cp]++;

            if (Arrays.equals(freqS, freqP))
                res.add(start + 1);

            start++;
            end++;
        }

        return res;
    }
}

```

```go

func findAnagrams(s string, p string) []int {
    n := len(s)
    m := len(p)

    res := make([]int, 0)

    if n < m {
        return res
    }

    freqS := [26]int{}
    freqP := [26]int{}

    for i := 0; i < m; i++ {
        freqS[s[i] - 'a']++
        freqP[p[i] - 'a']++
    }

    start := 0
    end := m

    if freqS == freqP {
        res = append(res, start)
    }

    for end < n {
        freqS[s[start] - 'a']--
        freqS[s[end] - 'a']++

        if freqS == freqP {
            res = append(res, start + 1)
        }

        start++
        end++
    }

    return res
}

```

```cpp

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;

        int n = s.length();
        int m = p.length();

        int freqS[26] = {0};
        int freqP[26] = {0};

        if (n < m) {
            return res;
        }

        for (int i = 0; i < m; i++) {
            freqS[(int)s[i] - 97]++;
            freqP[(int)p[i] - 97]++;
        }

        int start = 0;
        int end = m;

        if (std::equal(std::begin(freqS), std::end(freqS), std::begin(freqP))) {
            res.push_back(start);
        }

        while (end < n) {
            freqS[(int)s[start] - 97]--;
            freqS[(int)s[end] - 97]++;

            if (std::equal(std::begin(freqS), std::end(freqS),
                           std::begin(freqP))) {
                res.push_back(start + 1);
            }

            start++;
            end++;
        }

        return res;
    }
};

```

```rs

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let mut res = Vec::new();

        let n = s.len();
        let m = p.len();

        if n < m {
            return res;
        }

        let mut freq_s = [0; 26];
        let mut freq_p = [0; 26];

        for i in 0..m {
            let s_k = s.chars().nth(i).unwrap() as u32 - 'a' as u32;
            let p_k = p.chars().nth(i).unwrap() as u32 - 'a' as u32;

            freq_s[s_k as usize] += 1;
            freq_p[p_k as usize] += 1;
        }

        let mut start: usize = 0;
        let mut end: usize = m;

        if freq_s == freq_p {
            res.push(start as i32);
        }

        while end < n {
            let s_k = s.chars().nth(start).unwrap() as u32 - 'a' as u32;
            let p_k = s.chars().nth(end).unwrap() as u32 - 'a' as u32;

            freq_s[s_k as usize] -= 1;
            freq_s[p_k as usize] += 1;

            if freq_s == freq_p {
                res.push((start + 1) as i32);
            }

            start += 1;
            end += 1;
        }

        return res;
    }
}

```
