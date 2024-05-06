func trap(height []int) int {
	res, n := 0, len(height)-1
	l, r, lMax, rMax := 0, n, 0, height[n]

	for l <= r {
		lMax = max(height[l], lMax)
		rMax = max(height[r], rMax)

		if rMax >= lMax {
			res += lMax - height[l]
			l++
		} else {
			res += rMax - height[r]
			r--
		}
	}

	return res
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}