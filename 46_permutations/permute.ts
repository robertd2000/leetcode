function permute(nums: number[]): number[][] {
  return dfs(nums, [], []);
}

function dfs(nums: number[], path: number[], res: number[][]) {
  const n = nums.length;

  if (n === 0) {
    res.push([...path]);
  }

  for (let i = 0; i < n; i++) {
    const newNums = [...nums.slice(0, i), ...nums.slice(i + 1)];
    path.push(nums[i]);
    dfs(newNums, path, res);
    path.pop();
  }

  return res;
}
