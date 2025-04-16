class Solution {
  /**
   * @param {number[]} heights
   * @return {number}
   */
  largestRectangleArea(heights) {
    let maxArea = 0;

    const stack = [];

    heights.forEach((h, i) => {
      let start = i;

      while (stack.length && stack.at(-1).at(1) > h) {
        const [idx, height] = stack.pop();
        maxArea = Math.max(maxArea, height * (i - idx));
        start = idx;
      }

      stack.push([start, h]);
    });

    for (const [i, h] of stack) {
      maxArea = Math.max(maxArea, h * (heights.length - i));
    }

    return maxArea;
  }
}
