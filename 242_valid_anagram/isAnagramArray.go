func isAnagram(s string, t string) bool {
	n, m := len(s), len(t)
	BOUND := 97

	if n != m {
		return false
	}

	count := [26]int{}

	for _, c := range s {
		count[int(c)-BOUND]++
	}

	for _, c := range t {
		count[int(c)-BOUND]--

		if count[int(c)-BOUND] < 0 {
			return false
		}
	}

	return true
}