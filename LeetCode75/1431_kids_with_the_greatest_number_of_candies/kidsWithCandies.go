func kidsWithCandies(candies []int, extraCandies int) []bool {
	res := []bool{}
	maxNum := max(candies)

	for _, i := range candies {
		if i+extraCandies >= maxNum {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}

	return res
}

func max(list []int) int {
	maxNum := 0

	for _, i := range list {
		if i > maxNum {
			maxNum = i
		}
	}

	return maxNum
}
