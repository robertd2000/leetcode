package finalarraystateafterkmultiplicationoperationsi

func getFinalState(nums []int, k int, multiplier int) []int {
	for range k {
		idx := getMinIdx(nums)
		nums[idx] *= multiplier
	}

	return nums
}

func getMinIdx(nums []int) int {
	idx := 0
	min := nums[idx]

	for i, num := range nums {
		if num < min {
			min = num
			idx = i
		}
	}

	return idx
}
