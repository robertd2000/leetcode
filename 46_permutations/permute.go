func permute(nums []int) [][]int {
	answer := make([][]int, 0)
	aux(&answer, 0, nums)
	return answer
}

func aux(answer *[][]int, idx int, nums []int) {
	if idx == len(nums) {
		c := make([]int, len(nums))
		copy(c, nums)
		*answer = append(*answer, c)
		return
	}
	for i := idx; i < len(nums); i++ {
		nums[idx], nums[i] = nums[i], nums[idx]
		aux(answer, idx+1, nums)
		nums[i], nums[idx] = nums[idx], nums[i]
	}
	return
}