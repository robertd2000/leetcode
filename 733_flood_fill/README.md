[733. Flood Fill](https://leetcode.com/problems/flood-fill/)

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.

Return *the modified image after performing the flood fill*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

**Input:** image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
**Output:** [[2,2,2],[2,2,0],[2,0,1]]
**Explanation:** From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

**Example 2:**

**Input:** image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
**Output:** [[0,0,0],[0,0,0]]
**Explanation:** The starting pixel is already colored 0, so no changes are made to the image.

**Constraints:**

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 216`
- `0 <= sr < m`
- `0 <= sc < n`

Изображение представлено сеткой целых чисел `m x n` `image`, где `image[i][j]` представляет собой значение пикселя изображения.

Вам также даны три целых числа `sr`, `sc` и `color`. Вы должны выполнить **заливку** на изображении, начиная с пикселя `image[sr][sc]`.

Чтобы выполнить **заливку**, рассмотрите начальный пиксель, а также все пиксели, соединенные **4-направленно** с начальным пикселем того же цвета, что и начальный пиксель, а также все пиксели, соединенные **4-направленно** с этими пикселями (также того же цвета) и т. д. Замените цвет всех вышеупомянутых пикселей на `color`.

Верните _измененное изображение после выполнения заливки_.

**Пример 1:**

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

**Вход:** изображение = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, цвет = 2
**Выход:** [[2,2,2],[2,2,0],[2,0,1]]
**Объяснение:** Из центра изображения с позицией (sr, sc) = (1, 1) (т. е. красный пиксель) все пиксели, соединенные путем того же цвета, что и начальный пиксель (т. е. синие пиксели), окрашиваются в новый цвет.

Обратите внимание, что нижний угол не окрашен в 2, поскольку он не соединен с начальным пикселем в 4 направлениях.

**Пример 2:**

**Вход:** image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
**Выход:** [[0,0,0],[0,0,0]]
**Объяснение:** Начальный пиксель уже окрашен в 0, поэтому никаких изменений в изображение не вносится.

**Ограничения:**

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 216`
- `0 <= sr < m`
- `0 <= sc < n`

Задача решается с помощью рекурсии и поиска в глубину. Идея в том чтобы помечать элемент по заданным координатам и все его соседние элементы справа, слева, сверху и снизу рекурсивно.

Запомним в переменной prevColor в которую запишем изначальный цвет точки.
Создадим вспомогательную функцию mark, которая будет принимать координаты. В ней будем для начала проверять чтобы координаты не выходили за границы матрицы. Далее нужно проверить чтобы у точки по координатам был цвет, такой же как и изначальной точки. Иначе нужно будет выйти из функции:

```typescript
if (sr < 0 || sr >= m) return;
if (sc < 0 || sc >= n) return;
if (image[sr][sc] != prevColor) return;
```

Далее меняем цвет у точки по заданным координатам:

```typescript
image[sr][sc] = color;
```

После чего вызываем функцию mark рекурсивно для всех соседних точек:

```typescript
mark(sr, sc - 1);
mark(sr, sc + 1);
mark(sr - 1, sc);
mark(sr + 1, sc);
```

Итоговый код:

```typescript
function floodFill(
  image: number[][],
  sr: number,
  sc: number,
  color: number
): number[][] {
  const m = image.length;
  const n = image[0].length;

  const prevColor: number = image[sr][sc];

  if (prevColor === color) {
    return image;
  }

  function mark(sr: number, sc: number) {
    if (sr < 0 || sr >= m) return;
    if (sc < 0 || sc >= n) return;
    if (image[sr][sc] != prevColor) return;

    image[sr][sc] = color;

    mark(sr, sc - 1);
    mark(sr, sc + 1);
    mark(sr - 1, sc);
    mark(sr + 1, sc);
  }

  mark(sr, sc);

  return image;
}
```

```py

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        startColor = image[sr][sc]

        if startColor == color:
            return image

        def mark(row, col):
            if row < 0 or row >= m:
                return
            if col < 0 or col >= n:
                return
            if image[row][col] != startColor:
                return

            image[row][col] = color

            mark(row, col - 1)
            mark(row, col + 1)
            mark(row - 1, col)
            mark(row + 1, col)

        mark(sr, sc)

        return image

```

```go

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
		mark(row + 1, col)
	}
	mark(sr, sc)

	return image
}

```
