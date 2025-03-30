impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let mut res = Vec::new();

        let n = s.len();
        let m = p.len();

        if n < m {
            return res;
        }

        let mut freq_s = [0; 26];
        let mut freq_p = [0; 26];

        for i in 0..m {
            let s_k = s.chars().nth(i).unwrap() as u32 - 'a' as u32;
            let p_k = p.chars().nth(i).unwrap() as u32 - 'a' as u32;

            freq_s[s_k as usize] += 1;
            freq_p[p_k as usize] += 1;
        }
        
        let mut start: usize = 0;
        let mut end: usize = m;

        if freq_s == freq_p {
            res.push(start as i32);
        }

        while end < n {
            let s_k = s.chars().nth(start).unwrap() as u32 - 'a' as u32;
            let p_k = s.chars().nth(end).unwrap() as u32 - 'a' as u32;

            freq_s[s_k as usize] -= 1;
            freq_s[p_k as usize] += 1;

            if freq_s == freq_p {
                res.push((start + 1) as i32);
            }

            start += 1;
            end += 1;
        }

        return res;
    }
}