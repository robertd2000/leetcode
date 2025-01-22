# [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 \* 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

```py

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0

        m = len(flowerbed)
        start = 0 if flowerbed[0] == 0 else 1
        end = m if flowerbed[-1] == 0 else m - 1

        for i in range(start, end):
            if (
                (i == 0 or flowerbed[i - 1] == 0)
                and flowerbed[i] == 0
                and (i == m - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                k += 1
        return k >= n

```

```java

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int k = 0;
        int m = flowerbed.length;
        int start = flowerbed[0] == 0 ? 0 : 1;
        int end = flowerbed[m - 1] == 0 ? m : m - 1;

        for (int i = start; i < end; i++) {
            if ((i == 0 || flowerbed[i - 1] == 0) &&
                    flowerbed[i] == 0 &&
                    (i == m - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                k++;
            }
        }

        return k >= n;
    }
}

```
