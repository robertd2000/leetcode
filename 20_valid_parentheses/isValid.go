func isValid(s string) bool {
	var stack []rune
	p := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	for _, i := range s {
		if v, ok := p[i]; ok == true {
			if len(stack) > 0 && stack[len(stack)-1] == v {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, i)
		}
	}

	if len(stack) > 0 {
		return false
	}

	return true
}