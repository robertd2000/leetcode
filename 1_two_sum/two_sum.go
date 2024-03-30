package twosum

func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)

	for key, value := range nums {
		n := target - value

		if val, ok := hash[n]; ok {
			return []int{key, val}
		}

		hash[value] = key
	}

	panic("ERR")
}