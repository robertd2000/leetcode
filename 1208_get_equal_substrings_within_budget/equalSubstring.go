func equalSubstring(s string, t string, maxCost int) int {
	n := len(s)

	l, r := 0, 0

	for r = 0; r < n; r++ {
		maxCost -= abs(int(s[r]) - int(t[r]))
		if maxCost < 0 {
			maxCost += abs(int(s[l]) - int(t[l]))
			l++
		}
	}

	return r - l

}

func abs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}