func merge(intervals [][]int) [][]int {
	var res [][]int

	sort.Slice(intervals, func(i, j int) bool {
		if len(intervals[i]) == 0 && len(intervals[j]) == 0 {
			return false
		}
		if len(intervals[i]) == 0 || len(intervals[j]) == 0 {
			return len(intervals[i]) == 0
		}

		return intervals[i][0] < intervals[j][0]
	})

	res = append(res, intervals[0])

	for _, interval := range intervals {
		n := len(res) - 1
		if res[n][1] >= interval[0] {
			res[n][1] = max(res[n][1], interval[1])
		} else {
			res = append(res, interval)
		}
	}

	return res
}

func max(a int, b int) int {
	if a > b {
		return a
	}

	return b
}