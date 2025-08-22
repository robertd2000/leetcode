package reverseinteger

func reverse(x int) int {
	sign := 1

	if x < 0 {
		x = -x
		sign = -1
	}

	res := 0

	for x > 0 {
		digit := x % 10
		x = x / 10

		if res > 2147483647/10 {
			return 0
		}

		res = res*10 + digit
	}

	return res * sign
}