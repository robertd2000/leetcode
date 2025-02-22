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