package twosumsorted

func twoSum(numbers []int, target int) []int {
	l, r := 0, len(numbers)-1

	for l < r {
		if numbers[l]+numbers[r] == target {
			return []int{l + 1, r + 1}
		}
		if numbers[l]+numbers[r] > target {
			r = r - 1
		}
		if numbers[l]+numbers[r] < target {
			l = l + 1
		}
	}

	return []int{l, r}
}