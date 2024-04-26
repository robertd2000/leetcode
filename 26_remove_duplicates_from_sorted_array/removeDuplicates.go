func removeDuplicates(nums []int) int {
	idx := 0

	for _, val := range nums {
		if val != nums[idx] {
			idx++
			nums[idx] = val
		}
	}

	return idx + 1
}