class Solution {
    public String reversePrefix(String word, char ch) {
        int charIndex = word.indexOf(ch);

        String prefix = reverse(word.substring(0, charIndex + 1));
        String postfix = word.substring(charIndex + 1);

        return prefix + postfix;
    }

    private String reverse(String word) {
        String res = "";

        for (int i = word.length() - 1; i >= 0; i--) {
            res += word.charAt(i);
        }

        return res;
    }
}