func intersect(nums1 []int, nums2 []int) []int {
	hash := make(map[int]int)

	var res []int

	for _, num := range nums1 {
		hash[num] += 1
	}

	for _, num := range nums2 {
		if hash[num] > 0 {
			res = append(res, num)
		}
		hash[num] -= 1
	}

	return res
}