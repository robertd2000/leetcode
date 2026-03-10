use std::collections::HashMap;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let unique = get_unique(&nums);
        let curr_sum = sum(&nums);
        let unique_sum = sum(&unique);
        
        unique_sum * 2 - curr_sum
    }
}

fn sum(nums: &Vec<i32>) -> i32 {
    let mut sum = 0;

    for &v in nums {
        sum += v;
    }

    sum
}

fn get_unique(nums: &Vec<i32>) -> Vec<i32> {
        let mut h_map = HashMap::new();
        let mut res = Vec::new();

        for &v in nums {
            match h_map.get(&v) {
                Some(_) => (),
                _ => {
                    h_map.insert(v, true);
                    res.push(v);
                }
            }
        }

        res
}