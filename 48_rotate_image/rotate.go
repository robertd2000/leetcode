func rotate(matrix [][]int) {
	reverse(matrix)
    transpose(matrix)
}

func reverse(matrix [][]int) {
	l, r := 0, len(matrix)-1

	for l < r {
		matrix[l], matrix[r] = matrix[r], matrix[l]
		l++
		r--
	}
}

func transpose(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < i; j++ {
			matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
		}
	}
}