type Hash struct {
	Values       map[int]int
	DefaultValue int
}

func (h *Hash) GetOrDefault(key int) int {
	if val, ok := h.Values[key]; ok {
		return val
	}

	return h.DefaultValue
}

func (h *Hash) Set(key, value int) {
	h.Values[key] = value
}

func majorityElement(nums []int) int {
	hash := &Hash{
		Values:       make(map[int]int),
		DefaultValue: 0,
	}

	for _, i := range nums {
		val := hash.GetOrDefault(i) + 1
		hash.Set(i, val)
	}

	n := len(nums) / 2

	for key, value := range hash.Values {
		if value > n {
			return key
		}
	}

	return 0
}