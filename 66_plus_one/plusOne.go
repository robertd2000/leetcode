package plusone

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i]+1 < 10 {
			digits[i] += 1
			return digits
		}

		digits[i] = 0

		if i == 0 {
			res := []int{1}
			res = append(res, digits...)
			return res
		}
	}

	return digits
}
