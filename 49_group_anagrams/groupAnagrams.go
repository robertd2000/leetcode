package groupanagrams

import "slices"

func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]string)
	res := make([][]string, 0)

	for _, s := range strs {
		runes := []rune(s)
		slices.Sort(runes)
		key := string(runes)

		hashMap[key] = append(hashMap[key], s)
	}

	for _, v := range hashMap {
		res = append(res, v)
	}
	return res
}