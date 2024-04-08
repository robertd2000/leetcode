class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i = 0;
        List<String> result = new ArrayList<String>();

        int n = word1.length();
        int m = word2.length();

        while (i < n || i < m) {
            if (i < n) {
                String letter = Character.toString(word1.charAt(i));
                result.add(letter);
            }
            if (i < m) {
                String letter = Character.toString(word2.charAt(i));
                result.add(letter);
            }
            i++;
        }

        return String.join("", result);
    }
}