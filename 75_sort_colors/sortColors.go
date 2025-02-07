func sortColors(nums []int) {
	count := [3]int{}

	for _, num := range nums {
		count[num]++
	}

	k := 0

	for i := range 3 {
		for j := 0; j < count[i]; j++ {
			nums[k] = i
			k++
		}
	}
}