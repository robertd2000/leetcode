package movezeroes

func moveZeroes(nums []int) {
	l := 0

	for r := 0; r < len(nums); r++ {
		if nums[l] == 0 {
			nums[l], nums[r] = nums[r], nums[l]
		}

		if nums[l] != 0 {
			l++
		}
	}
}
