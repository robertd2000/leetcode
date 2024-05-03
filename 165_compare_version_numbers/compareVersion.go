func compareVersion(version1 string, version2 string) int {
	l1, l2 := strings.Split(version1, "."), strings.Split(version2, ".")

	n1, n2 := len(l1), len(l2)

	n := findMax(n1, n2)

	for i := range n {
		v1, v2 := 0, 0
		if i < n1 {
			v1, _ = strconv.Atoi(l1[i])
		}

		if i < n2 {
			v2, _ = strconv.Atoi(l2[i])
		}

		if v1 > v2 {
			return 1
		} else if v1 < v2 {
			return -1
		}
	}

	return 0
}

func findMax(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}