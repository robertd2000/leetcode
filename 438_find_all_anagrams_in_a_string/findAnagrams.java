class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();

        int n = s.length();
        int m = p.length();

        if (n < m)
            return res;

        int[] freqS = new int[26];
        int[] freqP = new int[26];

        for (int i = 0; i < m; i++) {
            int cs = s.charAt(i) - 'a';
            int cp = p.charAt(i) - 'a';
            freqS[cs]++;
            freqP[cp]++;
        }

        int start = 0;
        int end = m;

        if (Arrays.equals(freqS, freqP))
            res.add(start);

        while (end < n) {
            int cs = s.charAt(start) - 'a';
            int cp = s.charAt(end) - 'a';
            freqS[cs]--;
            freqS[cp]++;

            if (Arrays.equals(freqS, freqP))
                res.add(start + 1);

            start++;
            end++;
        }

        return res;
    }
}