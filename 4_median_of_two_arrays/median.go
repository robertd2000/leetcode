package medianoftwoarrays

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	i, j, k := 0, 0, 0
	n, m := len(nums1), len(nums2)
	r := n + m
	res := make([]int, r)

	for i < n && j < m {
		if nums1[i] < nums2[j] {
			res[k] = nums1[i]
			i++
		} else {
			res[k] = nums2[j]
			j++
		}
		k++
	}

	for i < n {
		res[k] = nums1[i]
		i++
		k++
	}

	for j < m {
		res[k] = nums2[j]
		j++
		k++
	}

	q := r / 2

	if r%2 == 0 {
		return float64(res[int(q)]+res[int(q)-1]) / 2.0
	}

	return float64(res[q])
}
