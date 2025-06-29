func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	var res strings.Builder

	for i := 0; i < len(strs[0]); i++ {
		currentChar := strs[0][i]
		for _, s := range strs[1:] {
			if i >= len(s) || s[i] != currentChar {
				return res.String()
			}
		}
		res.WriteByte(currentChar)
	}

	return res.String()
}