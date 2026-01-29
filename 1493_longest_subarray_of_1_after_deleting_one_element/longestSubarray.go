package main

func longestSubarray(nums []int) int {
	l, r := 0, 0
	c := 0

	for r < len(nums) {
		c += 1 - nums[r]
		if c > 1 {
			c -= 1 - nums[l]
			l++
		}

		r++
	}

	return r - l - 1
}
