[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the **longest**

**substring**

without repeating characters.

**Example 1:**

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3.

**Example 2:**

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

[3. Самая длинная подстрока без повторяющихся символов](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Для строки `s` найдите длину **самой длинной**

**подстроки**

без повторяющихся символов.

**Пример 1:**

**Вход:** s = "abcabcbb"
**Выход:** 3
**Объяснение:** Ответ: "abc", длина 3.

**Пример 2:**

**Вход:** s = "bbbbb"
**Выход:** 1
**Объяснение:** Ответ: "b", длина 1.

**Пример 3:**

**Вход:** s = "pwwkew"
**Выход:** 3
**Объяснение:** Ответ: "wke", длина 3.
Обратите внимание, что ответ должен быть подстрокой, "pwke" — это подпоследовательность, а не подстрока.

**Ограничения:**

- `0 <= s.length <= 5 * 104`
- `s` состоит из английских букв, цифр, символов и пробелов.

1. `Map` хранит символы как ключи, а их индексы как значения.
2. Мы по-прежнему поддерживаем указатели `left` и `right`, а также переменную `maxLength`.
3. Мы перебираем строку, используя указатель `right`.
4. Если текущего символа нет в карте или его индекс меньше `left`, это означает, что это новый уникальный символ.
5. Мы обновляем `charMap` индексом символа и обновляем `maxLength` при необходимости.
6. Если символ повторяется в текущей подстроке, мы перемещаем указатель `left` на следующую позицию после последнего вхождения символа.
7. Мы обновляем индекс текущего символа в `charMap` и продолжаем итерацию.
8. В конце мы возвращаем `maxLength` как длину самой длинной подстроки без повторяющихся символов.

То есть логика такая: создаем хэш таблицу map, в которой будем хранить буквы строки и их индексы. Также создаем 2 указателя - left и right. right указывает на текущий элемент строки, а left на начало подстроки. Итерируемся по строке и проверяем, встречался этот символ в строке или нет. Если его нет в map или его индекс (где он встречался в последний раз) меньше текущего начала подстроки left, то это новый, уникальный элемент в текущей подстроке (начинающейся с left). Значит нужно обновить map индексом символа, а также обновить maxLength. maxLength будет равен текущий индекс минус индекс начала текущей подстроки плюс 1:

```typescript
map[s[right]] = right;
maxLength = Math.max(maxLength, right - left + 1);
```

Иначе, если символ уже встречался в map и не является уникальным для данной подстроки, нужно обновить left - сдвинуть на следующую позицию относительно индекса встречавшегося в map символа:

```typescript
left = map[s[right]] + 1;
```

Далее нужно обновить значения в map:

```typescript
map[s[right]] = right;
```

Итоговый код:

```typescript
function lengthOfLongestSubstring(s: string): number {
  const map = {};
  const n = s.length;
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < n; right++) {
    if (!(s[right] in map) || map[s[right]] < left) {
      map[s[right]] = right;
      maxLength = Math.max(maxLength, right - left + 1);
    } else {
      left = map[s[right]] + 1;
      map[s[right]] = right;
    }
  }

  return maxLength;
}
```

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        n = len(s)
        l = 0
        maxLength = 0

        for r in range(n):
            if s[r] not in map or map[s[r]] < l:
                map[s[r]] = r
                maxLength = max(maxLength, r - l + 1)
            else:
                l = map[s[r]] + 1
                map[s[r]] = r

        return maxLength
```

```ts
function lengthOfLongestSubstring(s: string): number {
  const n = s.length;

  if (n === 0) return 0;

  let max = 0;

  const map = new Map<string, number>();

  let j = 0;

  for (let i = 0; i < n; i++) {
    const char = s[i];
    if (map.has(char)) {
      j = Math.max(j, (map.get(char) || 0) + 1);
    }

    map.set(char, i);
    max = Math.max(max, i - j + 1);
  }

  return max;
}
```

```go

func lengthOfLongestSubstring(s string) int {
    n := len(s)

    if n == 0 {
        return 0
    }

    longest := 0
    hash := make(map[rune]int)
    j := 0

    for i, c := range s {
        if val, ok := hash[c]; ok {
            j = max(j, val + 1)
        }

        hash[c] = i
        longest = max(longest, i - j + 1)
    }

    return longest
}

func max(a, b int) int {
    if a > b {
        return a
    }

    return b
}

```

```java

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0)
            return 0;
        int max = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0, j = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            max = Math.max(max, i - j + 1);
        }
        return max;
    }
}

```

```cpp

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();

        if (n == 0)
            return 0;

        int longest = 0;
        unordered_map<char, int> map;

        int j = 0;

        for (int i = 0; i < n; i++) {
            if (map.contains(s[i])) {
                j = max(j, map[s[i]] + 1);
            }
            map[s[i]] = i;
            longest = max(longest, i - j + 1);
        }

        return longest;
    }
};

```
