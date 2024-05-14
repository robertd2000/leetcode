func isAnagram(s string, t string) bool {
	n, m := len(s), len(t)

	if n != m {
		return false
	}

	hash := map[rune]int{}

	for _, c := range s {
		val := hash[c]
		hash[c] = val + 1
	}

	for _, c := range t {
		val := hash[c]
		hash[c] = val - 1

		if hash[c] < 0 {
			return false
		}
	}

	return true
}