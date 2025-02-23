func search(nums []int, target int) int {
	low := 0
	hight := len(nums) - 1

	for low <= hight {
		mid := int(low + ((hight - low) / 2))

		if nums[mid] == target {
			return mid
		}

		if nums[mid] < target {
			low = mid + 1
		}

		if nums[mid] > target {
			hight = mid - 1
		}
	}

	return -1
}