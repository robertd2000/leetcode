func majorityElement(nums []int) int {
	sort.Sort(sort.IntSlice(nums))
	n := len(nums) / 2

	return nums[n]
}