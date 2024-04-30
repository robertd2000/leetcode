func hIndex(citations []int) int {
	n := len(citations)

	buckets := make([]int, n+1)

	for _, c := range citations {
		if c >= n {
			buckets[n]++
		} else {
			buckets[c]++
		}
	}

	c := 0

	for i := n; i >= 0; i-- {
		c += buckets[i]
		if c >= i {
			return i
		}
	}
	return 0

}