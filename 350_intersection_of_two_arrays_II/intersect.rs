use std::collections::HashMap;

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut h_map: HashMap<i32, i32> = HashMap::new();
        let mut res = Vec::new();

        for num in nums1 {
            h_map.entry(num)
                .and_modify(|i| {*i+=1})
                .or_insert(1);
        }

        for num in nums2 {
            h_map.entry(num)
                .and_modify(|i| {
                    if *i > 0 {
                        res.push(num);
                    }
                    *i-=1;
                });
        }

        res
    }
}