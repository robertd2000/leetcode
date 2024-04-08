package maxarea

func maxArea(height []int) int {
	max := 0

	l, r := 0, len(height)-1

	for l < r {
		lHeight, rHeight := height[l], height[r]
		square := min(lHeight, rHeight) * (r - l)

		if square > max {
			max = square
		}

		if lHeight < rHeight {
			l++
		} else {
			r--
		}
	}

	return max
}

func min(first, second int) int {
	if first < second {
		return first
	}

	return second
}
