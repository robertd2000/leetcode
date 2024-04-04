func maxDepth(s string) int {
	curr, maxDepth := 0, 0

	for _, char := range s {
		if char == '(' {
			curr++
			maxDepth = max(curr, maxDepth)
		}
		if char == ')' {
			curr--
		}
	}

	return maxDepth
}

func max(first, second int) int {
	if first > second {
		return first
	}

	return second
}
