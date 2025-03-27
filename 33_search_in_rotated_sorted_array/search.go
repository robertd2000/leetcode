func search(nums []int, target int) int {
	n := len(nums)

	l, r := 0, n-1

	for l <= r {
		m := l + (r-l)/2

		if nums[m] == target {
			return m
		}

		if nums[l] <= nums[m] {
			if nums[m] >= target && nums[l] <= target {
				r = m - 1
			} else {
				l = m + 1
			}
		} else {
			if nums[m] <= target && target <= nums[r] {
				l = m + 1
			} else {
				r = m - 1
			}
		}
	}

	return -1
}