class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        }

        Map<Character, Integer> hash = new HashMap<>();

        for (char c : s.toCharArray()) {
            hash.put(c, hash.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            hash.put(c, hash.getOrDefault(c, 0) - 1);
            if (hash.getOrDefault(c, 0) < 0) {
                return false;
            }

        }
        
        return true;
    }
}