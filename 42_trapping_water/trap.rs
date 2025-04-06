use std::cmp;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        let mut res = 0;
        let mut l = 1;
        let mut r = n - 2;
        let mut lH = height[0];
        let mut rH = height[n - 1];

        while l <= r {
            if lH < rH {
                lH = cmp::max(lH, height[l]);
                res += lH - height[l];
                l += 1;
            } else {
                rH = cmp::max(rH, height[r]);
                res += rH - height[r];
                r -= 1;
            }
        }

        return res;
    }
}