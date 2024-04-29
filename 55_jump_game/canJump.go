func canJump(nums []int) bool {
	r, i, n := 0, 0, len(nums)

	for i = 0; i < n && i <= r; i++ {
		r = findMax(r, i+nums[i])
	}

	return i == n
}

func findMax(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}