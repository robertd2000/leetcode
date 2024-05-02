func productExceptSelf(nums []int) []int {
	pre, pos, n := 1, 1, len(nums)
	res := make([]int, n)

	fillArray(res, 1)

	for i := range nums {
		res[i] *= pre
		pre *= nums[i]

		res[n-i-1] *= pos
		pos *= nums[n-i-1]
	}

	return res
}

func fillArray(array []int, val int) {
	for i := range len(array) {
		array[i] = val
	}
}