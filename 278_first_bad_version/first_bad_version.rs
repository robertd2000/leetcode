// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
		let mut l = 1;
        let mut r = n;

        while l <= r {
            let mut m = l + (r - l) / 2;

            if self.isBadVersion(m) {
                r = m - 1
            } else {
                l = m + 1
            }
        }

        return l
    }
}