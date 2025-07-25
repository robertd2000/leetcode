func strStr(haystack string, needle string) int {
    n, m := len(haystack), len(needle)

    for i := 0; i < n - m + 1; i++ {
        if haystack[i: i + m] == needle {
            return i
        }
    }

    return -1
}