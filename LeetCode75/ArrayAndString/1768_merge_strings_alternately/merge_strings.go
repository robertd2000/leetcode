func mergeAlternately(word1 string, word2 string) string {
	i := 0
	n, m := len(word1), len(word2)
	res := ""

	for i < n || i < m {
		if i < n {
			res += string(word1[i])
		}
		if i < m {
			res += string(word2[i])
		}
		i++
	}

	return res
}