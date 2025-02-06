package main

func findCombinations(index, target int, candidates []int, current []int, result *[][]int) {
	if target == 0 {
		combination := make([]int, len(current))
		copy(combination, current)
		*result = append(*result, combination)
		return
	}

	for i := index; i < len(candidates); i++ {
		if candidates[i] <= target {
			current = append(current, candidates[i])
			findCombinations(i, target-candidates[i], candidates, current, result)
			current = current[:len(current)-1]
		}
	}
}

func combinationSum(candidates []int, target int) [][]int {
	result := make([][]int, 0)
	current := make([]int, 0)
	findCombinations(0, target, candidates, current, &result)
	return result
}
