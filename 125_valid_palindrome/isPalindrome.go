func isPalindrome(s string) bool {
	n := len(s)
	l, r := 0, n-1

	for l < r {
		lR, rR := rune(s[l]), rune(s[r])
		if !isAlphanumeric(lR) {
			l++
		}
		if !isAlphanumeric(rR) {
			r--
		}

		if isAlphanumeric(lR) && isAlphanumeric(rR) {
			if strings.ToLower(string(lR)) != strings.ToLower(string(rR)) {
				return false
			}

			l++
			r--
		}
	}

	return true
}

func isAlphanumeric(ch rune) bool {
	if unicode.IsLetter(ch) || unicode.IsDigit(ch) {
		return true
	}

	return false
}