func specialArray(nums []int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	n := len(nums)
	i := 0

	for i < n && nums[i] > i {
		i += 1
	}

	if i < n && i == nums[i] {
		return -1
	}

	return i
}