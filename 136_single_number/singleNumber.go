package singlenumber

func singleNumber(nums []int) int {
	unique := getUnique(nums)
	currSum := sum(nums)
	uniqueSum := sum(unique)

	return uniqueSum*2 - currSum
}

func sum(nums []int) int {
	s := 0

	for _, num := range nums {
		s += num
	}

	return s
}

func getUnique(nums []int) []int {
	res := make([]int, 0)
	set := make(map[int]bool)

	for _, num := range nums {
		if _, ok := set[num]; !ok {
			res = append(res, num)
		}

		set[num] = true
	}

	return res
}