func longestCommonPrefix(strs []string) string {
    sort.Strings(strs)

    var res strings.Builder

    first, last := strs[0], strs[len(strs) - 1]

    n := min(len(first), len(last))

    for i := 0; i < n; i++ {
        if first[i] != last[i] {
            return res.String()
        }

        res.WriteByte(first[i])
    }

    return res.String()
}