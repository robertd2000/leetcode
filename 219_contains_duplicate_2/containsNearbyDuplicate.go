func containsNearbyDuplicate(nums []int, k int) bool {
	hashMap := map[int]int{}

	for i, val := range nums {
		hashVal, ok := hashMap[val]
		if ok && i-hashVal <= k {
			return true
		}
		hashMap[val] = i
	}

	return false
}