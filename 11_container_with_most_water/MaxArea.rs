use std::cmp::Ordering;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        Self::max_area_acc(&height, 0, 0)
    }

    pub fn max_area_acc(heights: &[i32], acc: i32, max_height: i32) -> i32 {
        let len = heights.len();
        if heights.len() < 2 {
            return acc;
        }

        let mut i = 0;
        let mut j = len - 1;

        let first = loop {
            if i >= j {
                break max_height;
            }

            let first = heights[i];
            if first > max_height {
                break first;   
            }

            i += 1;
        };

        let last = loop {
            if i >= j {
                break max_height;
            }

            let last = heights[j];
            if last > max_height {
                break last;   
            }

            j -= 1;
        };

        let height = first.min(last);
        let width = (j - i) as i32;
        if width == 0 {
            return acc;
        }

        match first.cmp(&last) {
            Ordering::Less => {
                let height = first;
                let area = width * height;
                Self::max_area_acc(&heights[(i + 1)..(j + 1)], acc.max(area), height) // leave right
            },
            Ordering::Equal => {
                let height = first;
                let area = width * height;
                Self::max_area_acc(&heights[(i + 1)..j], acc.max(area), height) // dont leave anything
            },
            Ordering::Greater => {
                let height = last;
                let area = width * height;
                Self::max_area_acc(&heights[i..j], acc.max(area), height) // leave left
            },
        }
    }
}