var digits = map[byte]int{
	0x30: 0,
	0x31: 1,
	0x32: 2,
	0x33: 3,
	0x34: 4,
	0x35: 5,
	0x36: 6,
	0x37: 7,
	0x38: 8,
	0x39: 9,
}

func myAtoi(str string) int {
	res, sign, len, idx := 0, 1, len(str), 0

	// Skip leading spaces
	for idx < len && (str[idx] == ' ' || str[idx] == '\t') {
		idx++
	}

	if idx == len {
		return 0
	}

	// +/- Sign
	if str[idx] == '+' {
		sign = 1
		idx++
	} else if str[idx] == '-' {
		sign = -1
		idx++
	}

	// Digits: 0x30 = '0', 0x31 = '1', ... 0x39 = '9'
	for idx < len && str[idx] >= 0x30 && str[idx] <= 0x39 {
		res = res*10 + digits[str[idx]]
		if sign*res > math.MaxInt32 {
			return math.MaxInt32
		}

		if sign*res < math.MinInt32 {
			return math.MinInt32
		}

		idx++
	}

	return res * sign
}