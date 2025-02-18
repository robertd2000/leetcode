class Solution {
    public int longestPalindrome(String s) {
        int res = 0;
        int n = s.length();

        Set<Character> visited = new HashSet<>();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);

            if (visited.contains(c)) {
                res += 2;
                visited.remove(c);
            } else {
                visited.add(c);
            }
        }

        if (!visited.isEmpty()) res++;

        return res;
    }
}