func longestPalindrome(s string) int {
	res := 0

	visited := make(map[rune]bool)

	for _, c := range s {
		if _, ok := visited[c]; ok {
			res += 2
			delete(visited, c)
		} else {
			visited[c] = true
		}
	}

	if len(visited) > 0 {
		res++
	}

	return res
}