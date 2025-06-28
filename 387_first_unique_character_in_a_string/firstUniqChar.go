func firstUniqChar(s string) int {
	h := make(map[rune]int)

	for _, i := range s {
		h[i] += 1
	}

	for i, v := range s {
		if h[v] == 1 {
			return i
		}
	}

	return -1
}