# [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Example 1:

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

## Example 2:

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints:

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

**Follow up:**

- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

Можно использовать доп массив, в котором хранить оригинальные позиции в массиве. Пройтись от 0 до `k` и записать в начало массива значения `k` с конца - `temp[i + n - k]`. Потом пройтись от `k` до `n` и записать значения с начала массива - `nums[i] = temp[i - k]`

Можно обойтись без доп памяти - использовать повороты массива. Нужно найти правую границу - `r = k % n `, т.к. `k` может быть больше чем длинна массива `n`. Потом сделать 3 поворота - сначала повернуть весь массив, потом его левую часть до `r - 1` - тогда получится что конец из `k` элементов находится в начале массива. Затем повернуть конец массива.

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const n = nums.length;
  const r = k % n;

  reverse(nums, 0, n - 1);
  reverse(nums, 0, r - 1);
  reverse(nums, r, n - 1);
};

function reverse(nums, l, r) {
  while (l < r) {
    let temp = nums[l];
    nums[l] = nums[r];
    nums[r] = temp;
    l++;
    r--;
  }
}
```
