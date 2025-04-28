package floodfill

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	m, n := len(image), len(image[0])

	startColor := image[sr][sc]

	if startColor == color {
		return image
	}
	var mark func(int, int)
	mark = func(row int, col int) {
		if row < 0 || row >= m {
			return
		}

		if col < 0 || col >= n {
			return
		}

		if image[row][col] != startColor {
			return
		}

		image[row][col] = color

		mark(row, col-1)
		mark(row, col+1)
		mark(row-1, col)
		mark(row+1, col)
	}
	mark(sr, sc)

	return image
}
