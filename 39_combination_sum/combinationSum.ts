function combinationSum(candidates: number[], target: number): number[][] {
  const result = [];
  dfs(candidates, target, [], result);

  return result;
}

function dfs(
  nums: number[],
  target: number,
  path: number[],
  result: number[][]
) {
  if (target < 0) {
    return 0;
  }

  if (target === 0) {
    result.push(path);
    return;
  }

  for (let i = 0; i < nums.length; i++) {
    const newTarget = target - nums[i];
    const newPath = [...path, nums[i]];

    dfs(nums.slice(i), newTarget, newPath, result);
  }
}
