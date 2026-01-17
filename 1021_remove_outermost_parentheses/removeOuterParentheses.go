package removeoutermostparentheses

import "strings"

func removeOuterParentheses(s string) string {
	var sb strings.Builder
	op := 0

	for _, c := range s {
		if c == '(' && op > 0 {
			sb.WriteRune(c)
		}

		if c == ')' && op > 1 {
			sb.WriteRune(c)
		}

		if c == '(' {
			op++
		} else {
			op--
		}
	}

	return sb.String()
}
