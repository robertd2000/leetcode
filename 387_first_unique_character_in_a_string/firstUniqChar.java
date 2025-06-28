class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);        
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);        

            if (hashMap.get(c) == 1) return i;
        }

        return -1;
    }
}