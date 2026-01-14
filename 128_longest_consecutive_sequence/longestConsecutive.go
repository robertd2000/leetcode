package longestconsecutivesequence

func longestConsecutive(nums []int) int {
	set := make(map[int]struct{})

	for _, n := range nums {
		set[n] = struct{}{}
	}

	res := 0

	for x := range set {
		if _, ok := set[x-1]; ok {
			continue
		}

		y := x + 1

		for {
			if _, ok := set[y]; !ok {
				break
			}

			y += 1
		}

		res = max(res, y-x)
	}

	return res
}
